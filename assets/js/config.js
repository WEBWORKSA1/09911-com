/* =====================================================================
   09911.com — SITE CONFIG. Edit this file only; no build step needed.
   ===================================================================== */
window.SITE_CONFIG = {
  /* Form delivery (FormSubmit.co, free, no backend).
     The inbox address is never written in plain text anywhere on the site.
     STEP 1: first form submission sends an activation email to the inbox — click "Activate".
     STEP 2: FormSubmit then gives you a random alias string (e.g. "a1b2c3d4e5...").
             Paste it into FORM_ALIAS below. From then on the real address is not
             even present in encoded form. */
  FORM_ALIAS: "",
  _k: [116,118,106,53,115,112,104,116,110,71,56,104,122,114,121,118,126,105,108,126],

  /* Google AdSense — paste your publisher id (ca-pub-XXXXXXXXXXXXXXXX) to switch ad slots live.
     Also update /ads.txt with the same pub id. */
  ADSENSE_CLIENT: "",
  ADSENSE_SLOTS: { header: "", inContent: "", sidebar: "", footer: "" },

  /* Google Analytics 4 measurement id (G-XXXXXXX). Optional. */
  GA4_ID: "",

  /* YouTube: add video IDs (the part after watch?v=) to embed them. Empty = curated search cards. */
  YOUTUBE_CHANNEL_URL: "https://www.youtube.com/",
  YOUTUBE_VIDEOS: [],

  /* Donation links. Leave empty and the button falls back to the pledge form on /donate.html. */
  DONATE: { paypal: "", buymeacoffee: "", kofi: "", stripe: "", github_sponsors: "", upi: "" },

  /* Affiliate links per platform (fill with your tracked links; otherwise the public homepage is used). */
  AFFILIATE: {},

  CONTACT_URL: "https://web.works/contact"
};
