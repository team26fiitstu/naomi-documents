#!/usr/bin/env python3
"""Compile categorized LaTeX projects and create the website document index."""

import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "build" / "site"
CATEGORIES = {
    "zapisnice": "meeting",
    "retrospektivy": "retrospective",
    "progres": "progress",
    "metodiky": "methodology",
    "prirucky": "handbook",
    "vystupy": "deliverable",
}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def last_change(project: Path) -> int:
    paths = [str(project.relative_to(ROOT)), "assets"]
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", *paths],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    value = result.stdout.strip()
    if not value:
        value = subprocess.run(
            ["git", "log", "-1", "--format=%ct"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()
    if not value:
        raise ValueError(f"No Git timestamp for {project}")
    return int(value)


def read_metadata(project: Path) -> dict:
    with (project / "document.json").open(encoding="utf-8") as source:
        metadata = json.load(source)
    names = metadata.get("name")
    if not isinstance(names, dict) or any(
        not isinstance(names.get(locale), str) or not names[locale].strip()
        for locale in ("en", "sk")
    ):
        raise ValueError(f"{project}: document.json needs nonempty en and sk names")
    if "date" in metadata:
        datetime.strptime(metadata["date"], "%Y-%m-%d")
    return metadata


def discover() -> list[tuple[Path, str]]:
    projects = []
    for folder, kind in CATEGORIES.items():
        category = ROOT / folder
        for project in sorted(category.iterdir()):
            if project.is_dir():
                if not (project / "main.tex").is_file():
                    raise ValueError(f"Missing main.tex in {project}")
                projects.append((project, kind))
    known = {project / "main.tex" for project, _ in projects}
    unknown = [
        path for path in ROOT.rglob("main.tex")
        if path not in known and "build" not in path.relative_to(ROOT).parts
    ]
    if unknown:
        raise ValueError(f"Uncategorized LaTeX project: {unknown[0]}")
    if not projects:
        raise ValueError("No LaTeX projects found")
    return projects


def build() -> None:
    projects = discover()
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    docs = OUTPUT / "docs"
    docs.mkdir(parents=True)
    entries = []
    seen = set()

    for project, kind in projects:
        slug = project.name
        if not SLUG.fullmatch(slug) or slug in seen:
            raise ValueError(f"Invalid or duplicate document slug: {slug}")
        seen.add(slug)
        metadata = read_metadata(project)
        timestamp = last_change(project)
        date = metadata.get("date") or datetime.fromtimestamp(timestamp, timezone.utc).date().isoformat()
        environment = os.environ.copy()
        environment["SOURCE_DATE_EPOCH"] = str(timestamp)
        environment["FORCE_SOURCE_DATE"] = "1"

        print(f"Building {project.relative_to(ROOT)}", flush=True)
        result = subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "main.tex"],
            cwd=project, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        if result.returncode:
            print(result.stdout, file=sys.stderr)
            raise RuntimeError(f"LaTeX build failed: {project.relative_to(ROOT)}")
        pdf = project / "main.pdf"
        if not pdf.is_file() or pdf.stat().st_size == 0:
            raise ValueError(f"Invalid PDF: {pdf}")
        with pdf.open("rb") as compiled:
            if compiled.read(5) != b"%PDF-":
                raise ValueError(f"Invalid PDF: {pdf}")
        output_pdf = docs / f"{slug}.pdf"
        shutil.copy2(pdf, output_pdf)
        entries.append({
            "id": slug,
            "name": metadata["name"],
            "type": kind,
            "date": date,
            "pdf": f"docs/{slug}.pdf",
        })

    entries.sort(key=lambda item: (item["type"], item["name"]["en"].casefold()))
    (OUTPUT / "documents.json").write_text(
        json.dumps({"schemaVersion": 1, "documents": entries}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(entries)} PDFs and {OUTPUT.relative_to(ROOT) / 'documents.json'}")


if __name__ == "__main__":
    build()
