# Shared layout pieces for the static site generator (tools/build.py).
SITE = "https://09911.com"
CONTACT = "https://web.works/contact"

NAV = [
    ("index.html", "Home"), ("calendar.html", "Calendar"), ("9-9.html", "9.9"), ("11-11.html", "11.11"),
    ("festivals.html", "Festivals"), ("deals.html", "Deals"), ("numbers.html", "Lucky Numbers"),
    ("stats.html", "Stats"), ("videos.html", "Videos"), ("contests.html", "Contests"),
]


def head(title, desc, path, extra_ld=""):
    canon = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#e0242f">
<meta property="og:type" content="website"><meta property="og:site_name" content="09911">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"09911","url":"{SITE}/","description":"Festival-season shopping calendar, deal guides and Chinese lucky-number culture."}}</script>
{extra_ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(path):
    return f"""<div class="topbar" role="note">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="{CONTACT}" target="_blank" rel="noopener">contact us here</a></div>
<div id="site-header" data-page="{path}"></div>
<main id="main">
"""


def ad(kind="inContent"):
    return f'<div class="wrap"><div class="ad-slot" data-ad="{kind}" aria-label="Advertisement">Advertisement space · <a href="advertise.html">&nbsp;Sponsor this spot</a></div></div>'


def lead_box(title="", sub="", src="alerts"):
    t = f' data-title="{title}"' if title else ""
    d = f' data-sub="{sub}"' if sub else ""
    return f'<div data-leadbox="{src}"{t}{d}></div>'


def page_hero(title, sub, crumb):
    return f"""<section class="page-hero"><div class="wrap">
<div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
<h1>{title}</h1><p class="lead">{sub}</p>
</div></section>"""


def footer():
    return """</main>
<div id="site-footer"></div>
<script src="assets/js/config.js"></script>
<script src="assets/js/layout.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def faq_ld(pairs):
    import json
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    }, ensure_ascii=False) + "</script>"


def faq_html(pairs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs)
