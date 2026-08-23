# Associate – Foundations tutorial PDFs

Downloadable companion handbooks for the Associate Foundations console.

**Empty for now** — the `tutorials` array in `../assets/config.js` is `[]`, so the
console hides its Downloads section until the first PDF lands here.

This whole folder is copied verbatim into the deployed console by
`.github/workflows/pages.yml` (`cp -r ui/console-associate/. _site/associate-foundations/`),
so a file dropped here is immediately reachable at:

    https://jacinthpaul.github.io/Claude-Certified-Architect/associate-foundations/tutorials/<file>.pdf

## Adding another tutorial

1. Drop the PDF here using the naming convention
   `claude-certified-associate-foundations-tutorial-<n>.pdf`.
2. Add one entry to the `tutorials` array in `../assets/config.js` — that is
   the only place the console learns about it (title, blurb, pages, size).
3. Add one `<li>` to the Study material downloads list in `ui/hub/index.html`.
4. Bump the `?v=YYYYMMDDx` cache-bust query in `../index.html`.

No app code changes are needed — the console renders whatever `config.js` lists,
and hides the section entirely when the array is empty.
