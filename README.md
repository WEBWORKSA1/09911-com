# 09911.com: 9.9 → 11.11 Festival Season Hub

A static, responsive and fully monetizable website covering the world's double-date shopping festivals (9.9, 10.10, 11.11, 12.12, 618) and Chinese lucky-number culture. It is plain HTML, CSS and JS, and runs on the free GitHub Pages plan.

**Live (GitHub Pages):** https://webworksa1.github.io/09911-com/

## Features
- Live festival countdowns, a full-year calendar and one-click `.ics` reminders
- SEO hubs: 9.9 / 99 Mega Sale, 11.11 Singles' Day, all festivals, and sourced GMV statistics
- Interactive Chinese number luck checker, an 18-number library and a voucher-stacking calculator
- **Lead generation:**
  - Alert sign-ups on every page, an exit-intent modal and a sticky CTA
  - A dedicated Advertise / Partnership page with packages and a qualifying form
  - Deal, video, number-reading and job forms
- **Monetization:** AdSense slots (switch on in config), affiliate link overrides, YouTube embeds, sponsored placements
- **Donations** (4 tiers plus a pledge form), **contests** with rules, **careers** / creator program
- Dark mode, FAQ schema, Open Graph, sitemap, manifest, `prefers-reduced-motion` support
- The required interest bar at the top of every page links to https://web.works/contact

## Configure (edit `assets/js/config.js` only)
| Key | What to do |
|---|---|
| `FORM_ALIAS` | Submit any form once, then click **Activate** in the FormSubmit email. FormSubmit then issues a random alias: paste it here. After that, the inbox address is not present on the site even in encoded form. |
| `ADSENSE_CLIENT` / `ADSENSE_SLOTS` | Your `ca-pub-…` id (and optional slot ids). Also update `ads.txt`. |
| `GA4_ID` | Optional Google Analytics 4 id. |
| `YOUTUBE_VIDEOS`, `YOUTUBE_CHANNEL_URL` | Video IDs to embed, and your channel link. |
| `DONATE` | PayPal.me / Buy Me a Coffee / Ko-fi / Stripe / GitHub Sponsors links. |
| `AFFILIATE` | Tracked links keyed `shopee`, `lazada`, `aliexpress`, `taobao`, `jd`, `amazon`, `tiktok`, `temu`. |

The contact inbox is never written in plain text in any HTML or JS file, and there are no `mailto:` links.

## Edit content
- Header, footer, alert modal and lead boxes are shared from `assets/js/layout.js`, so one edit updates every page.
- Page bodies are generated from `tools/pages_a.py`, `tools/pages_b.py` and `tools/partials.py`:
```bash
cd tools && python3 build.py   # regenerates *.html and sitemap.xml in the repo root
```

## Hosting
The site is served by GitHub Pages from the `gh-pages` branch (root). `main` holds the same files plus the generator. After editing on `main`, copy the changes to `gh-pages`, or switch **Settings → Pages → Source** to `main` / root.

## Custom domain (09911.com)
1. Add a file named `CNAME` in the repo root containing `09911.com`. Only do this once DNS is ready, otherwise the github.io URL will redirect to a domain that isn't live yet.
2. DNS: apex `A` records → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; `www` `CNAME` → `webworksa1.github.io`.
3. Repo **Settings → Pages**: set the custom domain and tick **Enforce HTTPS**.

## Docs
- `docs/RESEARCH.md`: cultural and economic research, idea scoring, revenue model, 39-site audit
- `docs/BUILD-PROMPT.md`: the phase-wise build prompt

## Legal
Original content © 09911.com. Third-party names are used for identification only. See `legal.html`.
