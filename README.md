# NAOMI Documents

LaTeX sources for the NAOMI team's NAO Robot Exercise System documents. All documents use the team's NAOMI LaTeX template.

The documents cover the project description and goals, technical practices, version control, documentation, and backlog management.

## Compiled PDFs

- [Technical methodology](output/pdf/naomi-technical-methodology.pdf)
- [Version control methodology](output/pdf/naomi-version-control-methodology.pdf)
- [Documentation methodology](output/pdf/naomi-documentation-methodology.pdf)
- [Backlog management methodology](output/pdf/naomi-backlog-management-methodology.pdf)
- [Project description and goals](output/pdf/naomi-project-description-goals.pdf)

## Sources and naming

Each document has a directory named in kebab case, with `main.tex` as its entry point. Documents with references keep a `references.bib` beside the source. The two team logos live once in the root `assets/` directory. PDF files use `naomi-<document-directory>.pdf`.

To build one document locally, run `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from its directory. The generated `main.pdf` is ignored. To make standalone Overleaf imports, run `python3 scripts/package_overleaf.py` from the repository root, then upload a ZIP from `build/overleaf/` to Overleaf. ZIP files are generated locally and are not committed.
