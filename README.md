# NAOMI Methodologies

LaTeX sources for the NAOMI team's NAO Robot Exercise System methodologies. The documents use the team's [LaTeX template](https://github.com/team26fiitstu/naomi-latex-template).

## Documents

- `technical-methodology/` - coding conventions, version control, code review, and verification levels.
- `version-control-methodology/` - branch workflow, commits, pull requests, versions, and release tags.

Each directory is self-contained and includes `main.tex`, `references.bib`, and the required logo assets.

## Compiled PDFs

- [Technical methodology](output/pdf/naomi-technical-methodology.pdf)
- [Version control methodology](output/pdf/naomi-version-control-methodology.pdf)

## Build

Install a LaTeX distribution with `latexmk` and `biber`. From either document directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated `main.pdf` is ignored. Copy final builds to `output/pdf/` to update the PDFs committed to this repository. To remove LaTeX build files, run `latexmk -C` in that directory.
