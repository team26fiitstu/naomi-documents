# Technical Methodology

Coding conventions, version control, code review, and verification rules for the NAO Robot Exercise System.

## Open in Overleaf

Click the button to create an editable copy of this document in Overleaf.

[![Open in Overleaf](https://img.shields.io/badge/Open_in-Overleaf-47A141?logo=overleaf&logoColor=white)](https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/team26fiitstu/naomi-documents/main/output/overleaf/naomi-technical-methodology.zip)

[Download source ZIP](../output/overleaf/naomi-technical-methodology.zip)

## Build locally

Install a LaTeX distribution with `latexmk` and `biber`, then run in this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated `main.pdf` is ignored. The published PDF is in `../output/pdf/`. To update the Overleaf ZIP after editing the source, run `python3 ../scripts/package_overleaf.py` from this directory.
