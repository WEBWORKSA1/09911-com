# 09911.com — phase-wise build prompt

Copy each phase into your AI builder (Claude, Cursor, etc.) in order. Every phase builds on the repo from the previous one. The version in this repo was built from these phases.

---

## Global rules (paste at the top of every phase)

> You are building **09911.com**, a static site: HTML, CSS and vanilla JS only. No backend, and it must deploy on the free GitHub Pages plan. It is a **global shopping-festival season hub** (9.9 → 10.10 → 11.11 → 12.12, 618, Chinese festivals) combined with **Chinese lucky-number culture**.
>
> **Brand:** "09911": 0 → 9.9 → 11.11. Palette red #e0242f, orange #ff6a13, gold #e8a317/#ffd35a, ink #140c08, warm off-white #fffaf5. Fonts: Space Grotesk (display) and Inter (body). Mobile-first, dark mode, WCAG AA, no horizontal scroll at 360px.
>
> **Hard requirements:**
> 1. Every page's topmost element is a bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linking to https://web.works/contact.
> 2. All forms deliver to a single inbox via FormSubmit AJAX. The address must **never** appear in HTML, visible text or plain-text JS. Store it encoded (char-code shift + reverse) and decode only at submit time, and support a `FORM_ALIAS` config that replaces it once FormSubmit issues one. No `mailto:` links anywhere.
> 3. All site-owner settings (AdSense id, GA4, YouTube IDs, donation links, affiliate links) live in `assets/js/config.js`. Ad slots and embeds degrade gracefully when empty.
> 4. No third-party logos. Use platform and festival names nominatively only. Include a trademark and copyright disclosure, and never claim rights over the numbers.
> 5. Never invent prices, reviews, testimonials, member counts or live-activity notices. Every statistic must be cited.

---

## Phase 1 — Research and information architecture
> Produce `docs/RESEARCH.md`:
> - The meaning of 0, 9, 99, 11 and 09911 in Mandarin (homophones, Double Ninth, Singles' Day origin)
> - The economic scale of 11.11 and 9.9, with sources
> - A scored comparison of at least 4 site ideas
> - A revenue model
> - An audit of at least 35 reference sites (deal, coupon, cashback, price-tracker, festival and numerology sites) listing their features, forms, content, design and monetization
>
> Output the sitemap: Home, Calendar, 9.9, 11.11, Festivals, Deals, Lucky Numbers, Stats, Videos, Contests, Advertise, Donate, Careers, About, Contact, Legal, 404.

## Phase 2 — Design system and layout shell
> Create `assets/css/style.css` with CSS custom properties, light/dark themes (system default plus a toggle saved in localStorage) and these components:
> - buttons, cards, badges (Hot, Live, Verified, Sponsored, Gold, Soon), chips
> - countdown card, lead box, forms, segmented checkboxes
> - tables in scroll wrappers, FAQ accordions, timeline, bar chart, pricing tiers
> - modal, toast, sticky CTA, reveal-on-scroll (respecting `prefers-reduced-motion`)
>
> Build a Python generator (`tools/build.py` + `partials.py`) that outputs static pages with a shared head (SEO meta, Open Graph, canonical, WebSite JSON-LD), the mandatory top bar, a sticky header with a mobile menu, and a footer with a legal note.

## Phase 3 — Festival engine and countdowns
> In `main.js`:
> - Generate events for this year and next: the monthly double dates, 9.9 + 99 Mega Sale, 11.11, 12.12, 618, 520, Black Friday (4th Friday of November), Cyber Monday, plus a lunar table (CNY, Qixi, Mid-Autumn, Chongyang, Dragon Boat) for 2026–2028. All go-live times are 00:00 UTC+8.
> - Homepage hero countdown with festival chips and a LIVE state lasting 24 hours.
> - Calendar page timeline with filters.
> - One-click `.ics` download (single event or all upcoming) with a 12-hour reminder alarm.

## Phase 4 — Content hubs (SEO)
> Write long-form hubs for **9.9** (Shopee/99 history, why 9 = 久, Chongyang, a 6-step playbook) and **11.11**:
> - 1993 origin and the Alibaba 2009 → 2021 GMV story
> - Syntun 2025 figures
> - A pre-sale phase table and the 4-layer stacking method
>
> Also build a Festivals overview (618, 520, Qixi, 10.10, Black Friday, 12.12, CNY, Mid-Autumn), a Stats page with a CSS bar chart and a sourced table, and FAQPage JSON-LD on every hub. Add a sitemap.xml, robots.txt and manifest.

## Phase 5 — Interactive tools
> Build:
> 1. A **Chinese number luck checker**: digit cards, a homophone dictionary, combo phrases (1314, 520, 168, 518, 888, 666, 99, 88, 11, 14, 250, 514, 748), a 0–100 meter, a dominant digit and an entertainment disclaimer.
> 2. A **voucher-stacking calculator**: list price, platform voucher, shop voucher, bank %, portal % and the 30-day low, giving an effective price and a verdict.
> 3. A number library of 18 cards with anchors.

## Phase 6 — Lead generation (highest priority for revenue)
> - A lead box on most pages for festival alerts: email, country, festival selector, platform checkboxes, consent. Include a honeypot field. Reveal a success state and fire a GA4 `generate_lead` event.
> - An exit-intent / 45-second modal, shown once per visitor and never after they convert.
> - A sticky "Alerts" button.
> - A dedicated **Advertise** page: value props, 4 packages (Featured Deal $49/wk, Festival Takeover $499, Newsletter & Video $199, Title Partner / Domain custom), a 3-step process, a qualifying form (interest, company, site, festival, budget, goals, consent), domain-acquisition CTA to web.works/contact, FAQ schema.
> - Secondary lead forms: deal submission, number-reading request, creator video submission, job application, contact form (topic selector).

## Phase 7 — Monetization
> - AdSense: `.ad-slot` placeholders (header, in-content, sidebar, footer) that become responsive `<ins class="adsbygoogle">` units when `ADSENSE_CLIENT` is set, plus an `ads.txt` template.
> - Affiliate: `data-aff` links overridden from config, `rel="sponsored"`, affiliate disclosure.
> - YouTube: click-to-load privacy embeds (youtube-nocookie) from `YOUTUBE_VIDEOS`, falling back to curated YouTube search cards, plus a Subscribe button.
> - Sponsored badges and "Sponsor this spot" links in empty ad slots.

## Phase 8 — Community: donations, contests, hiring
> - **Donate:** 4 tiers ($9 Lucky 9, $19 Double Nine, $99 Forever, monthly) mapped to PayPal / BMC / Ko-fi / GitHub Sponsors from config, falling back to a pledge form. Show an allocation bar chart (Ops 30, Talent 25, Prizes 20, Marketing 15, Promo 10) and a not-tax-deductible notice.
> - **Contests:** 11.11 giveaway ($99 + $11 + $11), Creator Challenge, Deal Hunter of the Month. The entry form has a skill question and 18+ consent. Rules summary: no purchase necessary, void where prohibited, random draw.
> - **Careers:** 6 remote roles and an application form.

## Phase 9 — Legal, trust, performance, QA
> - Legal page: trademark and copyright disclosure (09911 is a domain and numeric identifier with no claim over numbers; not affiliated with "911" or emergency services; third-party marks and festival names used nominatively), affiliate and advertising disclosure, privacy (FormSubmit, AdSense cookies, GA4, local storage, rights), terms (information only, contest terms, donations, no warranty).
> - QA:
>   - Playwright at 1366px and 390px on every page, with no overflow and no console errors
>   - Mocked form submission
>   - Grep the repo to confirm the inbox address is not present in plain text
>   - Lighthouse score of 90+

## Phase 10 — Deploy and grow
> - Push to `github.com/webworksa1/09911-com`, branch `main`, including `.nojekyll`. Enable Pages (branch `main`, root).
> - Custom domain: add a `CNAME` file containing `09911.com`. Point apex A records to 185.199.108.153 / .109.153 / .110.153 / .111.153 and `www` CNAME to `webworksa1.github.io`, then enable HTTPS.
> - After launch:
>   - Submit the sitemap to Search Console and apply for AdSense
>   - Activate FormSubmit and paste the alias into config
>   - Publish one festival guide per double date
>   - Grow the alert list before every 11.11
>   - Add zh/ms/id/th/vi translations as the next expansion
