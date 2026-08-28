/* CCAF Exam Prep Console — runtime config.
   The Associate console is fully static: lesson walkthroughs are claude.ai chat
   transcripts baked into data.js, so there is no live backend to call. */
window.CCAF_CONFIG = {
  live: false,

  // Downloadable tutorial handbooks for THIS course — same contract as the
  // Architect console (see ui/console/assets/config.js). Empty until the first
  // Associate PDF lands in ui/console-associate/tutorials/; while empty the
  // console's Downloads section is hidden.
  tutorials: [],
};
