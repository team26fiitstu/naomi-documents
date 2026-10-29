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

## PDF pipeline

Run `python3 scripts/build_documents.py` locally after installing `latexmk`, `biber`, `lmodern`, and the TeX packages. It compiles every categorized document into `build/site/docs/` and writes `build/site/documents.json` with name, type, date, and PDF link. The checked-in PDFs under `output/pdf/` are historical snapshots; the pipeline builds from LaTeX sources.

`.github/workflows/publish-methodologies.yml` runs on pull requests and on every push that changes a LaTeX source, bibliography, metadata, shared asset, or pipeline script. It uploads the generated files as a review artifact, synchronizes them into a temporary website checkout, checks links, and builds the website. A successful `main` run commits changed PDFs and the index to the website repository, which then deploys through its normal Pages workflow. Removed documents are removed from the website only if they were listed in the previous generated index; website-managed PDFs are preserved.

### One-time rollout

1. Merge the website changes that read `public/documents.json` and validate its PDF links.
2. Register a GitHub App owned by `team26fiitstu` for document publication. Give it only **Contents: Read and write**, disable unused webhooks, and install it on **only** `team26fiitstu.github.io`.
3. In the website repository's `Main Branch Protection` ruleset, add only this GitHub App to the bypass list with **Always allow**. The ruleset requires pull requests for other actors, so publication cannot push to `main` without this narrowly scoped bypass.
4. In `team26fiitstu/naomi-documents`, store the app's Client ID as the Actions variable `SITE_APP_CLIENT_ID` and its PEM private key as the Actions secret `SITE_APP_PRIVATE_KEY`. Do not commit the private key or paste it into an issue or PR.
5. Merge this workflow to `main`, then use **Run workflow** once. Verify the generated website commit, Pages deployment, and PDF links for both languages. After successful publication, remove the old `SITE_REPO_TOKEN` secret and revoke its personal access token.

The built-in `GITHUB_TOKEN` cannot write to the website repository. The workflow instead creates a short-lived GitHub App installation token scoped to the website repository and `contents:write`; its push triggers the website's Pages workflow.
