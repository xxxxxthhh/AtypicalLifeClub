#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
# ─── How to run ───
# python3 static/invest/research/generate_feed.py

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Final, Union


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
FEED_XML: Final = ROOT / "feed.xml"
SITE_URL: Final = "https://atypicallife.club"
CHANNEL_LINK: Final = f"{SITE_URL}/invest/research/"
CHANNEL_TITLE: Final = "Atypical Life Club · 研究报告 / Research Reports"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_reports() -> list[dict[str, Json]]:
    try:
        data = json.loads(REPORTS_JSON.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {REPORTS_JSON}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {REPORTS_JSON}: {exc}")
    if not isinstance(data, list):
        fail("reports.json must be an array")
    reports: list[dict[str, Json]] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            fail(f"reports.json[{index}] must be an object")
        reports.append(item)
    return reports


def require_string(report: dict[str, Json], key: str) -> str:
    value = report.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{report.get('id', '<unknown>')} missing {key}")
    return value


def update_day(report: dict[str, Json]) -> str:
    value = report.get("lastUpdate") or report.get("date")
    if not isinstance(value, str) or not value.strip():
        fail(f"{report.get('id', '<unknown>')} missing lastUpdate/date")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        fail(f"{report.get('id', '<unknown>')} has invalid lastUpdate/date: {value}")
    return value


def pub_date(day: str) -> str:
    dt = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return format_datetime(dt, usegmt=True)


def absolute_url(path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    if not path.startswith("/"):
        path = f"/{path}"
    return f"{SITE_URL}{path}"


def item_title(report: dict[str, Json]) -> str:
    title = require_string(report, "title")
    title_en = report.get("titleEn")
    if isinstance(title_en, str) and title_en.strip():
        return f"{title} / {title_en}"
    return title


def build_feed(reports: list[dict[str, Json]]) -> ET.ElementTree:
    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = CHANNEL_TITLE
    ET.SubElement(channel, "link").text = CHANNEL_LINK
    ET.SubElement(channel, "description").text = "Company research updates from Atypical Life Club."
    ET.SubElement(channel, "language").text = "zh-CN"

    sorted_reports = sorted(reports, key=update_day, reverse=True)[:50]
    for report in sorted_reports:
        report_id = require_string(report, "id")
        day = update_day(report)
        link = absolute_url(require_string(report, "file"))
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = item_title(report)
        ET.SubElement(item, "link").text = link
        guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
        guid.text = f"{link}#{report_id}@{day}"
        ET.SubElement(item, "pubDate").text = pub_date(day)
        summary = report.get("summary")
        ET.SubElement(item, "description").text = summary if isinstance(summary, str) else ""

    ET.indent(rss, space="  ")
    return ET.ElementTree(rss)


def main() -> None:
    tree = build_feed(load_reports())
    tree.write(FEED_XML, encoding="utf-8", xml_declaration=True, short_empty_elements=False)
    text = FEED_XML.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        FEED_XML.write_text(f"{text}\n", encoding="utf-8")
    print(f"OK: generated {FEED_XML}")


if __name__ == "__main__":
    main()
