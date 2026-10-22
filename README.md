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

- [Technical methodology: Open in Overleaf](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fraw.githubusercontent.com%2Fteam26fiitstu%2Fnaomi-methodologies%2Fmain%2Foutput%2Foverleaf%2Fnaomi-technical-methodology.zip&main_document=main.tex&engine=pdflatex) ([download ZIP](output/overleaf/naomi-technical-methodology.zip))
- [Version control methodology: Open in Overleaf](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fraw.githubusercontent.com%2Fteam26fiitstu%2Fnaomi-methodologies%2Fmain%2Foutput%2Foverleaf%2Fnaomi-version-control-methodology.zip&main_document=main.tex&engine=pdflatex) ([download ZIP](output/overleaf/naomi-version-control-methodology.zip))

Each link creates a separate editable Overleaf project from the current source. It is a copy, not an automatic GitHub sync. To refresh the ZIP files after source changes, run `python3 scripts/package_overleaf.py` and commit the regenerated files.

## Build

Install a LaTeX distribution with `latexmk` and `biber`. From either document directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated `main.pdf` is ignored. Copy final builds to `output/pdf/` to update the PDFs committed to this repository. To remove LaTeX build files, run `latexmk -C` in that directory.
