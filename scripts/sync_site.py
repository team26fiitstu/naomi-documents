#!/usr/bin/env python3
"""Copy generated PDFs and their index into a website checkout."""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "build" / "site"
PDF_LINK = re.compile(r"^docs/[a-z0-9]+(?:-[a-z0-9]+)*\.pdf$")


def links(index: Path) -> set[str]:
    data = json.loads(index.read_text(encoding="utf-8"))
    if data.get("schemaVersion") != 1 or not isinstance(data.get("documents"), list):
        raise ValueError(f"Invalid document index: {index}")
    result = {entry["pdf"] for entry in data["documents"]}
    if not all(PDF_LINK.fullmatch(link) for link in result):
        raise ValueError(f"Unsafe PDF path in {index}")
    return result


def main(website: Path) -> None:
    public = website / "public"
    if not public.is_dir():
        raise ValueError(f"Not a website checkout: {website}")
    current = public / "documents.json"
    previous = links(current) if current.exists() else set()
    published = links(SOURCE / "documents.json")
    for link in previous - published:
        (public / link).unlink(missing_ok=True)
    for link in published:
        shutil.copy2(SOURCE / link, public / link)
    shutil.copy2(SOURCE / "documents.json", current)
    print(f"Synchronized {len(published)} PDFs to {website}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: sync_site.py WEBSITE_CHECKOUT")
    main(Path(sys.argv[1]).resolve())
