#!/usr/bin/env python3
"""Regenerate validated data on the latest branch tip and push without force.

The caller supplies a command that BOTH regenerates and validates the allowlisted
outputs. Every attempt runs in its own worktree; neither a rejected commit nor
stale generated JSON is replayed over another writer's changes.
"""

import argparse
from pathlib import Path
import subprocess
import sys
import tempfile
import time


class PublicationError(RuntimeError):
    pass


def git(repo, *args, check=True):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], text=True, capture_output=True
    )
    if check and result.returncode:
        raise PublicationError(result.stderr.strip() or result.stdout.strip())
    return result


def remote_tip(repo, remote, branch):
    git(repo, "fetch", "--no-tags", remote, f"refs/heads/{branch}")
    return git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()


def changed_paths(repo):
    tracked = git(repo, "diff", "--name-only", "--no-renames", "-z", "HEAD").stdout
    staged = git(repo, "diff", "--cached", "--name-only", "--no-renames", "-z").stdout
    untracked = git(repo, "ls-files", "--others", "--exclude-standard", "-z").stdout
    return set(filter(None, (tracked + staged + untracked).split("\0")))


def publish(args):
    repo = Path(git(Path.cwd(), "rev-parse", "--show-toplevel").stdout.strip())
    git(repo, "check-ref-format", f"refs/heads/{args.branch}")
    allowed = set(args.path)
    for path in allowed:
        if Path(path).is_absolute() or ".." in Path(path).parts or path.startswith("-"):
            raise PublicationError(f"Output path must be repository-relative: {path}")
        if str(Path(path)) != path or path == ".":
            raise PublicationError(f"Output path must be a normalized file path: {path}")
    base = remote_tip(repo, args.remote, args.branch)
    for attempt in range(1, args.attempts + 1):
        print(f"Publication attempt {attempt}/{args.attempts} from {base}", flush=True)
        with tempfile.TemporaryDirectory(prefix="publish-data-") as temp:
            worktree = Path(temp) / "worktree"
            git(repo, "worktree", "add", "--detach", str(worktree), base)
            try:
                result = subprocess.run(args.command, cwd=worktree)
                if result.returncode:
                    raise PublicationError(
                        f"Generation/validation failed ({result.returncode}); nothing published"
                    )
                unexpected = changed_paths(worktree) - allowed
                if unexpected:
                    raise PublicationError(
                        "Refusing unexpected output changes: " + ", ".join(sorted(unexpected))
                    )
                git(worktree, "add", "--", *args.path)
                diff = git(worktree, "diff", "--cached", "--quiet", check=False)
                if diff.returncode == 0:
                    latest = remote_tip(repo, args.remote, args.branch)
                    if latest == base:
                        print("Validated data is unchanged; nothing to publish", flush=True)
                        return
                    if git(repo, "merge-base", "--is-ancestor", base, latest, check=False).returncode:
                        raise PublicationError("Remote history was rewritten; refusing automatic recovery")
                    if attempt == args.attempts:
                        raise PublicationError("Remote kept advancing during no-op checks; rerun on latest branch")
                    print("Remote advanced during generation; rechecking latest inputs", flush=True)
                    base = latest
                    time.sleep(args.retry_delay * attempt)
                    continue
                if diff.returncode != 1:
                    raise PublicationError(diff.stderr.strip() or "Could not inspect staged data")
                git(worktree, "commit", "-m", args.message)
                candidate = git(worktree, "rev-parse", "HEAD").stdout.strip()
                push = git(
                    worktree, "push", "--porcelain", args.remote,
                    f"HEAD:refs/heads/{args.branch}", check=False,
                )
                print(push.stdout, end="", flush=True)
                if push.stderr:
                    print(push.stderr, end="", file=sys.stderr, flush=True)
                latest = remote_tip(repo, args.remote, args.branch)
                # Verify remote state even when transport acknowledgement was lost.
                published = git(repo, "merge-base", "--is-ancestor", candidate, latest, check=False)
                if published.returncode == 0:
                    print(f"Published and verified {candidate} on {args.branch}", flush=True)
                    return
                if push.returncode == 0:
                    raise PublicationError("Push succeeded but remote no longer contains the commit")
                if latest == base:
                    raise PublicationError(
                        "Push rejected without a newer remote commit; check permissions, "
                        "branch rules, or service availability"
                    )
                if git(repo, "merge-base", "--is-ancestor", base, latest, check=False).returncode:
                    raise PublicationError("Remote history was rewritten; refusing automatic recovery")
                if attempt == args.attempts:
                    raise PublicationError(
                        f"Remote kept advancing across {args.attempts} attempts; nothing overwritten. "
                        "Rerun this workflow from the latest branch"
                    )
                print("Remote advanced; discarding candidate and regenerating on latest data", flush=True)
                base = latest
            finally:
                # Only remove the temporary worktree owned by this attempt.
                git(repo, "worktree", "remove", "--force", str(worktree))
        time.sleep(args.retry_delay * attempt)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--message", required=True)
    parser.add_argument("--path", action="append", required=True)
    parser.add_argument("--attempts", type=int, default=4)
    parser.add_argument("--retry-delay", type=float, default=2)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    if not args.command or not 1 <= args.attempts <= 10 or args.retry_delay < 0:
        parser.error("Require a command, 1–10 attempts, and a non-negative retry delay")
    try:
        publish(args)
    except (PublicationError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
