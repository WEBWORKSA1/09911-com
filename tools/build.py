#!/usr/bin/env python3
"""Static site generator for 09911.com. Run: python3 tools/build.py  (writes HTML to repo root)."""
import os
from partials import head, header, footer, ad, lead_box, page_hero, faq_ld, faq_html, CONTACT
from pages_a import PAGES_A
from pages_b import PAGES_B

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render(path, title, desc, body, ld=""):
    html = head(title, desc, path, ld) + header(path) + body + footer()
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(html)
    return path


if __name__ == "__main__":
    built = []
    for p in PAGES_A + PAGES_B:
        built.append(render(*p))
    # sitemap
    urls = "".join(
        f"<url><loc>https://09911.com/{'' if p == 'index.html' else p}</loc><changefreq>weekly</changefreq><priority>{'1.0' if p == 'index.html' else '0.8'}</priority></url>"
        for p in built if p != "404.html")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>\n")
    print("Built:", ", ".join(built))
