/* CCA Exam Prep Console — runtime config.
   Controls whether the console calls a live backend (api_server.py) to run the
   real repo demos, or falls back to the simulated output baked into data.js. */
window.CCA_CONFIG = {
  // Try the live backend first. If the fetch fails (e.g. opened as a static
  // file with no server), the console silently falls back to simulated output.
  live: true,

  // Base URL of the api_server. Empty string = same origin (recommended:
  // serve index.html FROM api_server.py so this just works).
  // If you run the API on a different port, set e.g. "http://127.0.0.1:8000".
  apiBase: "",

  // Build the run URL for a task id ("2.4") or scenario number.
  runUrl(id) { return `${this.apiBase}/api/run?task=${encodeURIComponent(id)}`; },
  scenarioUrl(n) { return `${this.apiBase}/api/run?scenario=${encodeURIComponent(n)}`; },

  // Downloadable tutorial handbooks for THIS course. Paths are relative to the
  // console folder, which the Pages workflow copies verbatim, so each file is
  // served from /<course>/tutorials/<file>.pdf. Add one entry per PDF; an empty
  // list hides the console's Downloads section entirely.
  tutorials: [
    {
      title: "Tutorial 1 — Foundations handbook",
      blurb: "The full Architect Foundations walkthrough in print form: the five exam domains, the architecture patterns behind them, and worked examples you can read away from the console.",
      file: "tutorials/claude-certified-architect-foundations-tutorial-1.pdf",
      meta: "PDF · 41 pages · 0.9 MB",
    },
  ],
};
