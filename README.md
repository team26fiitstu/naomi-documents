# NAOMI Methodologies

LaTeX sources for the NAOMI team's NAO Robot Exercise System methodologies. The documents use the team's [LaTeX template](https://github.com/team26fiitstu/naomi-latex-template).

## Documents

- `technical-methodology/` - coding conventions, version control, code review, and verification levels.
- `version-control-methodology/` - branch workflow, commits, pull requests, versions, and release tags.

Each directory is self-contained and includes `main.tex`, `references.bib`, and the required logo assets.

## Build

Install a LaTeX distribution with `latexmk` and `biber`. From either document directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated `main.pdf` is a local build artifact and is not committed. To remove LaTeX build files, run `latexmk -C` in that directory.
