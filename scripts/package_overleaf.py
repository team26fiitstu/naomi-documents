#!/usr/bin/env python3
"""Create standalone Overleaf ZIPs from the methodology sources."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "overleaf"
PROJECTS = {
    "technical-methodology": "naomi-technical-methodology.zip",
    "version-control-methodology": "naomi-version-control-methodology.zip",
}


def add_file(archive: ZipFile, source: Path, name: str) -> None:
    info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for directory, filename in PROJECTS.items():
        project = ROOT / directory
        files = [project / "main.tex", project / "references.bib"]
        files.extend(sorted((project / "assets").glob("*.png")))
        target = OUTPUT / filename
        with ZipFile(target, "w") as archive:
            for source in files:
                add_file(archive, source, source.relative_to(project).as_posix())
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
