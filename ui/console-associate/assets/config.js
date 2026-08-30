/* CCAF Exam Prep Console — runtime config.
   The Associate console is fully static: lesson walkthroughs are claude.ai chat
   transcripts baked into data.js, so there is no live backend to call. */
window.CCAF_CONFIG = {
  live: false,

  // Downloadable tutorial handbooks for THIS course — same contract as the
  // Architect console (see ui/console/assets/config.js). Paths are relative to
  // the console folder, which the Pages workflow copies verbatim, so each file
  // is served from /associate-foundations/tutorials/<file>.pdf. An empty list
  // hides the console's Downloads section entirely.
  tutorials: [
    {
      title: "Tutorial 1 — Foundations handbook",
      blurb: "The full Associate Foundations walkthrough in print form: the seven exam domains, all 30 blueprint objectives, and the judgment the CCAO-F exam tests — plus a cheat sheet and a two-week study plan.",
      file: "tutorials/claude-certified-associate-foundations-tutorial-1.pdf",
      meta: "PDF · 37 pages · 1.0 MB",
    },
  ],
};
