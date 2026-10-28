# NAOMI Documents

LaTeX sources for the NAOMI team's NAO Robot Exercise System documents. All documents use the team's NAOMI LaTeX template.

The documents cover the project description and goals, technical practices, version control, documentation, and backlog management.

## Compiled PDFs

- [Technical methodology](output/pdf/naomi-technical-methodology.pdf)
- [Version control methodology](output/pdf/naomi-version-control-methodology.pdf)
- [Documentation methodology](output/pdf/naomi-documentation-methodology.pdf)
- [Backlog management methodology](output/pdf/naomi-backlog-management-methodology.pdf)
- [Project description and goals](output/pdf/naomi-project-description-goals.pdf)
- [Definition of done](output/pdf/naomi_definition_of_done.pdf)

## Sources and naming

Document type is determined by the top-level folder:

| Folder | Website section |
|---|---|
| `zapisnice/` | Meeting minutes |
| `retrospektivy/` | Retrospectives |
| `progres/` | Progress reports |
| `metodiky/` | Methodologies |
| `prirucky/` | Handbooks |
| `vystupy/` | Deliverables |

Create a kebab-case directory under the appropriate type with `main.tex` and `document.json`. The metadata contains localized names and may set the document date:

```json
{
  "name": { "en": "Sprint 01 minutes", "sk": "Zápisnica zo šprintu 01" },
  "date": "2026-11-10"
}
```

When `date` is omitted, the index uses the date of the latest Git change to the document or shared `assets/`. The slug must be unique across all types. Bibliography files stay beside `main.tex`; the team logos are shared under `assets/`.

## Overleaf and GitHub

GitHub is the publication source. This repository contains several independent LaTeX projects, while Overleaf's direct GitHub synchronization links one Overleaf project to one repository. It is a premium feature, the push from Overleaf is manual, and an existing Overleaf project cannot be directly linked to an existing GitHub repository. For this repository, use the reliable manual path: download the Overleaf source ZIP, copy its `.tex`, bibliography, and local assets into the matching document directory, then commit and push through a pull request. Keep `document.json` in the GitHub directory. A separate mirror repository per Overleaf project is possible if the team later adopts premium Git integration.

For the existing documents, `python3 scripts/package_overleaf.py` creates standalone imports in `build/overleaf/`. These ZIPs are generated locally and are not committed.

## PDF pipeline

Run `python3 scripts/build_documents.py` locally after installing `latexmk`, `biber`, and the TeX packages. It compiles every categorized document into `build/site/docs/` and writes `build/site/documents.json` with name, type, date, and PDF link. The checked-in PDFs under `output/pdf/` are historical snapshots; the pipeline builds from LaTeX sources.

`.github/workflows/publish-methodologies.yml` runs on pull requests and on every push that changes a LaTeX source, bibliography, metadata, shared asset, or pipeline script. It uploads the generated files as a review artifact, synchronizes them into a temporary website checkout, checks links, and builds the website. A successful `main` run commits changed PDFs and the index to the website repository, which then deploys through its normal Pages workflow. Removed documents are removed from the website only if they were listed in the previous generated index; website-managed PDFs are preserved.

### One-time rollout

1. Merge the website changes that read `public/documents.json` and validate its PDF links.
2. Create a fine-grained personal access token limited to `team26fiitstu/team26fiitstu.github.io` with **Contents: Read and write**. Its owner must be allowed to push to the website's `main` branch. Store it as the Actions secret `SITE_REPO_TOKEN` in `team26fiitstu/naomi-documents`.
3. Merge this workflow to `main`, then use **Run workflow** once. Verify the generated website commit, Pages deployment, and PDF links for both languages.

The default `GITHUB_TOKEN` cannot write to the website repository and its commits would not trigger the website's push workflow. A GitHub App installation token is a better team-owned replacement for the personal token once available.
