# NAOMI Methodologies

LaTeX sources for the NAOMI team's NAO Robot Exercise System methodologies. The documents use the team's [LaTeX template](https://github.com/team26fiitstu/naomi-latex-template).

## Documents

- `technical-methodology/` - coding conventions, version control, code review, and verification levels.
- `version-control-methodology/` - branch workflow, commits, pull requests, versions, and release tags.

Each directory is self-contained and includes `main.tex`, `references.bib`, and the required logo assets.

## Compiled PDFs

- [Technical methodology](output/pdf/naomi-technical-methodology.pdf)
- [Version control methodology](output/pdf/naomi-version-control-methodology.pdf)

## Open in Overleaf

Click a button below to create a separate editable Overleaf project for each methodology.

### Technical methodology

[![Open in Overleaf](https://img.shields.io/badge/Open_in-Overleaf-47A141?logo=overleaf&logoColor=white)](https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/team26fiitstu/naomi-methodologies/main/output/overleaf/naomi-technical-methodology.zip)

[Download source ZIP](output/overleaf/naomi-technical-methodology.zip)

### Version control methodology

[![Open in Overleaf](https://img.shields.io/badge/Open_in-Overleaf-47A141?logo=overleaf&logoColor=white)](https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/team26fiitstu/naomi-methodologies/main/output/overleaf/naomi-version-control-methodology.zip)

[Download source ZIP](output/overleaf/naomi-version-control-methodology.zip)

These buttons load ZIP files from `main`, so new or updated ZIPs become available through them after the corresponding PR is merged. For a pre-merge preview, open a branch-specific ZIP URL with the same Overleaf API. An imported Overleaf project is an editable copy and does not synchronize later GitHub changes automatically. After changing the LaTeX sources, run `python3 scripts/package_overleaf.py` and commit the regenerated ZIP files.

## Build

Install a LaTeX distribution with `latexmk` and `biber`. From either document directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated `main.pdf` is ignored. Copy final builds to `output/pdf/` to update the PDFs committed to this repository. To remove LaTeX build files, run `latexmk -C` in that directory.
