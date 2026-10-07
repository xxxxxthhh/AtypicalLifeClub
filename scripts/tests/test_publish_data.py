"""Offline integration tests for safe, regenerating data publication.

Each test uses a bare remote and two real clones. A pre-push hook advances the
remote between generation and push, making the race deterministic without a
network service or timing-dependent background processes.
"""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


PUBLISHER = Path(__file__).resolve().parents[1] / "publish_data.py"
DATA_PATH = "data/historical.json"
SECOND_PATH = "data/summary.json"


GENERATOR = textwrap.dedent(
    r"""
    import json
    import os
    from pathlib import Path
    import subprocess
    import sys

    data_path = Path("data/historical.json")
    rows = json.loads(data_path.read_text())
    mode = os.environ.get("TEST_GENERATOR_MODE", "normal")
    branch = subprocess.run(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
        text=True, capture_output=True,
    ).stdout.strip()
    record = {
        "cwd": str(Path.cwd()),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "branch": branch,
        "rows_before": rows[:],
    }
    with Path(os.environ["TEST_GENERATOR_LOG"]).open("a") as log:
        log.write(json.dumps(record) + "\n")

    if mode == "noop-race":
        subprocess.run(
            [sys.executable, os.environ["TEST_RACE_HOOK"], "--during-generation"],
            check=True,
        )

    if mode == "generator-failure":
        data_path.write_text('["partial output"]\n')
        sys.exit(7)
    if mode == "invalid-output":
        data_path.write_text("invalid JSON\n")
    elif mode not in ("noop", "noop-race"):
        if "generated" not in rows:
            rows.append("generated")
        data_path.write_text(json.dumps(rows, indent=2) + "\n")

    if mode == "unexpected-tracked":
        Path("README.md").write_text("unapproved generator edit\n")
    if mode == "unexpected-staged":
        path = Path("README.md")
        original = path.read_text()
        path.write_text("unexpected staged output\n")
        subprocess.run(["git", "add", "README.md"], check=True)
        path.write_text(original)
    if mode == "unexpected-untracked":
        Path("unexpected.txt").write_text("must not be silently omitted\n")
    if mode == "ignored-output":
        Path("cache.tmp").write_text("ignored cache\n")
    if mode == "two-paths":
        Path("data/summary.json").write_text('{"updated": true}\n')

    # Validation is part of the regeneration command. A failure must prevent
    # every push, including a push of the partially modified output above.
    validated = json.loads(data_path.read_text())
    assert isinstance(validated, list)
    assert all(isinstance(row, str) for row in validated)
    """
)


PRE_PUSH_HOOK = textwrap.dedent(
    r"""
    import json
    import os
    from pathlib import Path
    import subprocess
    import sys

    during_generation = "--during-generation" in sys.argv[1:]
    log_key = "TEST_GENERATOR_RACE_LOG" if during_generation else "TEST_PUSH_LOG"
    races_key = "TEST_GENERATOR_RACES" if during_generation else "TEST_RACES"
    log = Path(os.environ[log_key])
    attempts = json.loads(log.read_text()) if log.exists() else []
    attempts.append(len(attempts) + 1)
    log.write_text(json.dumps(attempts))
    races = json.loads(os.environ.get(races_key, "[]"))
    if len(attempts) <= len(races):
        writer = Path(os.environ["TEST_WRITER"])
        # Hooks inherit repository-specific Git variables. Do not let the
        # publisher worktree's index or GIT_DIR leak into the other clone.
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        env["GIT_CONFIG_NOSYSTEM"] = "1"
        env["GIT_TERMINAL_PROMPT"] = "0"

        def git(*args):
            return subprocess.check_output(
                ["git", *args], cwd=writer, env=env, text=True,
                stderr=subprocess.STDOUT,
            ).strip()

        git("fetch", "origin", "main")
        git("reset", "--hard", "origin/main")
        row = "remote-" + str(len(attempts))
        if races[len(attempts) - 1] == "same-file":
            path = writer / "data/historical.json"
            rows = json.loads(path.read_text())
            rows.append(row)
            path.write_text(json.dumps(rows, indent=2) + "\n")
            git("add", "data/historical.json")
        else:
            path = writer / "README.md"
            path.write_text(path.read_text() + row + "\n")
            git("add", "README.md")
        git("commit", "-m", "Concurrent writer " + row)
        git("push", "origin", "HEAD:refs/heads/main")
        with Path(os.environ["TEST_REMOTE_HEADS"]).open("a") as heads:
            heads.write(git("rev-parse", "HEAD") + "\n")
    """
)


@unittest.skipUnless(shutil.which("git"), "git is required")
class PublishDataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="publish-data-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / "remote.git"
        self.caller = self.root / "caller"
        self.writer = self.root / "writer"
        self.generator_log = self.root / "generator.jsonl"
        self.push_log = self.root / "push.json"
        self.remote_heads = self.root / "remote-heads.txt"
        home = self.root / "home"
        home.mkdir()
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith("GIT_")
        }
        self.env.update({
            "HOME": str(home),
            "XDG_CONFIG_HOME": str(home / ".config"),
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
            "TEST_GENERATOR_LOG": str(self.generator_log),
            "TEST_PUSH_LOG": str(self.push_log),
            "TEST_WRITER": str(self.writer),
            "TEST_REMOTE_HEADS": str(self.remote_heads),
            "TEST_GENERATOR_RACE_LOG": str(self.root / "generator-races.json"),
            "TEST_RACE_HOOK": str(self.caller / ".git/hooks/pre-push"),
        })
        self.git("init", "--bare", "--initial-branch=main", str(self.remote), cwd=self.root)
        self.git("clone", str(self.remote), str(self.caller), cwd=self.root)
        self.configure(self.caller)
        (self.caller / "data").mkdir()
        (self.caller / DATA_PATH).write_text('[\n  "seed"\n]\n')
        (self.caller / SECOND_PATH).write_text('{"updated": false}\n')
        (self.caller / "README.md").write_text("original readme\n")
        (self.caller / "other.txt").write_text("original other file\n")
        (self.caller / ".gitignore").write_text("*.tmp\n")
        (self.caller / "regenerate.py").write_text(GENERATOR)
        self.git("add", ".")
        self.git("commit", "-m", "Initial fixture")
        self.git("push", "-u", "origin", "main")
        self.initial_head = self.git("rev-parse", "HEAD")
        self.git("clone", str(self.remote), str(self.writer), cwd=self.root)
        self.configure(self.writer)
        hook = self.caller / ".git/hooks/pre-push"
        hook.write_text(f"#!{sys.executable}\n" + PRE_PUSH_HOOK)
        hook.chmod(0o755)

    def git(self, *args, cwd=None):
        result = subprocess.run(
            ["git", *args], cwd=cwd or self.caller, env=self.env,
            text=True, capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def configure(self, repo):
        self.git("config", "user.name", "Publisher Test", cwd=repo)
        self.git("config", "user.email", "publisher-test@example.invalid", cwd=repo)
        self.git("config", "commit.gpgsign", "false", cwd=repo)

    def publish(self, *, mode="normal", races=(), generation_races=(), attempts=4, paths=(DATA_PATH,)):
        caller_head = self.git("rev-parse", "HEAD")
        caller_branch = self.git("symbolic-ref", "--short", "HEAD")
        command = [
            sys.executable, str(PUBLISHER), "--branch", "main",
            "--remote", "origin", "--message", "Publish test data",
            "--attempts", str(attempts), "--retry-delay", "0",
        ]
        for path in paths:
            command.extend(["--path", path])
        command.extend(["--", sys.executable, "regenerate.py"])
        result = subprocess.run(
            command, cwd=self.caller,
            env={
                **self.env,
                "TEST_GENERATOR_MODE": mode,
                "TEST_RACES": json.dumps(races),
                "TEST_GENERATOR_RACES": json.dumps(generation_races),
            },
            text=True, capture_output=True, timeout=60,
        )
        # All exit paths must clean up temporary worktrees without detaching
        # or switching the caller's own checkout.
        worktrees = self.git("worktree", "list", "--porcelain")
        self.assertEqual(worktrees.count("worktree "), 1, worktrees)
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), caller_branch)
        self.assertEqual(self.git("rev-parse", "HEAD"), caller_head)
        return result

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_failure(self, result):
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def remote_head(self):
        return self.git("--git-dir", str(self.remote), "rev-parse", "main")

    def remote_file(self, path):
        return self.git("--git-dir", str(self.remote), "show", f"main:{path}")

    def runs(self):
        if not self.generator_log.exists():
            return []
        return [json.loads(line) for line in self.generator_log.read_text().splitlines()]

    def pushes(self):
        return json.loads(self.push_log.read_text()) if self.push_log.exists() else []

    def assert_detached_runs(self, count):
        runs = self.runs()
        self.assertEqual(len(runs), count)
        for run in runs:
            self.assertEqual(run["branch"], "", run)
            self.assertNotEqual(Path(run["cwd"]), self.caller)
            self.assertFalse(Path(run["cwd"]).exists(), "Temporary worktree was not removed")
        return runs

    def test_publishes_only_allowed_data_on_first_attempt(self):
        self.assert_success(self.publish())
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "generated"])
        self.assertEqual(self.remote_file("README.md"), "original readme")
        changed = self.git("--git-dir", str(self.remote), "diff-tree", "--no-commit-id", "--name-only", "-r", "main")
        self.assertEqual(changed, DATA_PATH)
        self.assertEqual(self.pushes(), [1])
        runs = self.assert_detached_runs(1)
        self.assertEqual(runs[0]["head"], self.initial_head)

    def test_unrelated_remote_commit_survives_rejected_push(self):
        self.assert_success(self.publish(races=["unrelated"]))
        self.assertEqual(self.remote_file("README.md"), "original readme\nremote-1")
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "generated"])
        self.assertEqual(self.pushes(), [1, 2])
        runs = self.assert_detached_runs(2)
        self.assertEqual(runs[1]["head"], self.remote_heads.read_text().strip())

    def test_same_file_race_regenerates_and_preserves_other_writers_rows(self):
        self.assert_success(self.publish(races=["same-file"]))
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1", "generated"])
        runs = self.assert_detached_runs(2)
        self.assertEqual(runs[0]["rows_before"], ["seed"])
        self.assertEqual(runs[1]["rows_before"], ["seed", "remote-1"])
        self.assertEqual(self.pushes(), [1, 2])

    def test_two_remote_advances_succeed_within_retry_budget(self):
        self.assert_success(self.publish(races=["same-file", "same-file"], attempts=3))
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1", "remote-2", "generated"])
        runs = self.assert_detached_runs(3)
        self.assertEqual([run["head"] for run in runs[1:]], self.remote_heads.read_text().splitlines())
        self.assertEqual(self.pushes(), [1, 2, 3])

    def test_two_remote_advances_exhaust_retry_budget_without_overwrite(self):
        self.assert_failure(self.publish(races=["same-file", "same-file"], attempts=2))
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1", "remote-2"])
        self.assertEqual(self.pushes(), [1, 2])
        self.assert_detached_runs(2)
        self.assertEqual(self.remote_head(), self.remote_heads.read_text().splitlines()[-1])

    def test_generator_failure_never_pushes_partial_output(self):
        self.assert_failure(self.publish(mode="generator-failure"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_invalid_output_never_pushes(self):
        self.assert_failure(self.publish(mode="invalid-output"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_noop_succeeds_without_commit_or_push(self):
        self.assert_success(self.publish(mode="noop"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_noop_refetches_and_revalidates_when_remote_advances_during_generation(self):
        self.assert_success(self.publish(mode="noop-race", generation_races=["same-file"]))
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1"])
        self.assertEqual(self.pushes(), [])
        runs = self.assert_detached_runs(2)
        self.assertEqual(runs[1]["head"], self.remote_head())
        self.assertEqual(runs[1]["rows_before"], ["seed", "remote-1"])

    def test_noop_remote_advances_respect_retry_budget(self):
        self.assert_failure(self.publish(
            mode="noop-race", generation_races=["same-file", "same-file"], attempts=2,
        ))
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1", "remote-2"])
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(2)

    def test_unchanged_remote_rejection_is_not_retried(self):
        hook = self.remote / "hooks/update"
        hook.write_text("#!/bin/sh\necho 'Deliberate server policy rejection' >&2\nexit 1\n")
        hook.chmod(0o755)
        self.assert_failure(self.publish(attempts=4))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [1])
        self.assert_detached_runs(1)

    def test_unexpected_tracked_change_fails_before_push(self):
        self.assert_failure(self.publish(mode="unexpected-tracked"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_unexpected_nonignored_untracked_file_fails_before_push(self):
        self.assert_failure(self.publish(mode="unexpected-untracked"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_unexpected_staged_change_cannot_hide_behind_clean_worktree(self):
        self.assert_failure(self.publish(mode="unexpected-staged"))
        self.assertEqual(self.remote_head(), self.initial_head)
        self.assertEqual(self.pushes(), [])
        self.assert_detached_runs(1)

    def test_ignored_generated_file_is_not_published(self):
        self.assert_success(self.publish(mode="ignored-output"))
        self.assertNotIn("cache.tmp", self.git("--git-dir", str(self.remote), "ls-tree", "-r", "--name-only", "main").splitlines())
        self.assertEqual(self.pushes(), [1])

    def test_repeatable_paths_publish_both_expected_files(self):
        self.assert_success(self.publish(mode="two-paths", paths=(DATA_PATH, SECOND_PATH)))
        self.assertEqual(json.loads(self.remote_file(SECOND_PATH)), {"updated": True})
        changed = self.git("--git-dir", str(self.remote), "diff-tree", "--no-commit-id", "--name-only", "-r", "main")
        self.assertEqual(set(changed.splitlines()), {DATA_PATH, SECOND_PATH})

    def test_dirty_callers_index_files_and_branch_are_preserved(self):
        (self.caller / "other.txt").write_text("user staged edit\n")
        self.git("add", "other.txt")
        (self.caller / "README.md").write_text("user unstaged edit\n")
        (self.caller / DATA_PATH).write_text("user's unfinished data edit\n")
        (self.caller / "untracked.txt").write_text("user untracked content\n")
        before_status = self.git("status", "--porcelain")
        before_index = self.git("diff", "--cached", "--binary")
        before_worktree = self.git("diff", "--binary")
        self.assert_success(self.publish(races=["same-file"]))
        self.assertEqual(self.git("status", "--porcelain"), before_status)
        self.assertEqual(self.git("diff", "--cached", "--binary"), before_index)
        self.assertEqual(self.git("diff", "--binary"), before_worktree)
        self.assertEqual((self.caller / "untracked.txt").read_text(), "user untracked content\n")
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "remote-1", "generated"])

    def test_unpushed_feature_branch_is_preserved_and_not_used_as_input(self):
        self.git("switch", "-c", "user-feature")
        (self.caller / DATA_PATH).write_text('["unpublished user data"]\n')
        self.git("add", DATA_PATH)
        self.git("commit", "-m", "Unpublished feature work")
        self.assert_success(self.publish())
        self.assertEqual(json.loads(self.remote_file(DATA_PATH)), ["seed", "generated"])
        self.assertEqual(json.loads((self.caller / DATA_PATH).read_text()), ["unpublished user data"])
        runs = self.assert_detached_runs(1)
        self.assertEqual(runs[0]["head"], self.initial_head)


if __name__ == "__main__":
    unittest.main()
