# NAOMI Documents

## PDFs

- [Technical methodology](https://team26fiitstu.github.io/docs/technical-methodology.pdf)
- [Version control methodology](https://team26fiitstu.github.io/docs/version-control-methodology.pdf)
- [Documentation methodology](https://team26fiitstu.github.io/docs/documentation-methodology.pdf)
- [Backlog management methodology](https://team26fiitstu.github.io/docs/backlog-management-methodology.pdf)
- [Definition of done](https://team26fiitstu.github.io/docs/definition-of-done.pdf)
- [Project description and goals](https://team26fiitstu.github.io/docs/project-description-goals.pdf)

## Sources and naming

The top-level folder determines where a document appears on the website:

| Folder | Website section |
|---|---|
| `zapisnice/` | Meeting minutes |
| `retrospektivy/` | Retrospectives |
| `progres/` | Progress reports |
| `metodiky/` | Methodologies |
| `prirucky/` | Handbooks |
| `vystupy/` | Deliverables |

Each document lives in a uniquely named kebab-case directory, for example `metodiky/new-methodology/`. It needs `main.tex` and `document.json`. Bibliography files stay beside `main.tex`; shared logos are in `assets/`.

`document.json` provides the English and Slovak website titles. The date is optional; without it, the website uses the date of the latest Git change to the document or shared assets.

```json
{
  "name": { "en": "New methodology", "sk": "Nová metodika" },
  "date": "2026-11-10"
}
```

## Create or update a document

1. For a new document, choose a folder from the table, create a directory with a unique kebab-case name, and add `main.tex` and `document.json`. Use an existing document as a LaTeX example. To update a document, edit its `.tex`, bibliography, metadata, or assets.
2. If LaTeX is installed locally, run `python3 scripts/build_documents.py` to compile all documents and check the generated PDFs in `build/site/docs/`.
3. Commit the source changes and open a pull request. CI compiles the PDFs and checks the website. After the pull request is merged into `main`, the PDFs and document index are published to the website automatically. Edit the LaTeX sources rather than the generated PDFs.
