from partials import ad, lead_box, page_hero, faq_ld, faq_html, CONTACT

PLATFORMS = [
    ("Shopee", "shopee", "https://shopee.com/", "SG · MY · PH · TH · VN · ID · TW · BR", "Pioneered 9.9 in 2016. Free-shipping vouchers, Coins cashback, Shopee Live flash deals."),
    ("Lazada", "lazada", "https://www.lazada.com/", "SG · MY · PH · TH · VN · ID", "Alibaba-backed. Collect-and-stack vouchers, LazMall brand deals, 11.11 & 12.12 flagship events."),
    ("AliExpress", "aliexpress", "https://www.aliexpress.com/", "Global (200+ markets)", "Cross-border 11.11 Global Shopping Festival; coins, store coupons and 'Choice' free shipping."),
    ("Taobao / Tmall", "taobao", "https://world.taobao.com/", "China + global shipping", "Home of the 99 sale and the original 11.11. Pre-sale deposits, cross-store discounts."),
    ("JD.com", "jd", "https://global.jd.com/", "China", "Anchors the 618 mid-year festival; strong on electronics and fast logistics."),
    ("Amazon", "amazon", "https://www.amazon.com/", "Global", "Runs Prime Big Deal Days in October plus Black Friday — the West's answer to 11.11."),
    ("TikTok Shop", "tiktok", "https://shop.tiktok.com/", "US · UK · SEA", "Live-commerce heavy; 9.9/11.11/12.12 campaigns with creator-exclusive codes."),
    ("Temu", "temu", "https://www.temu.com/", "Global", "Deep-discount marketplace running near-permanent sale events and new-user coupons."),
]


def platform_cards(n=8):
    out = []
    for name, key, url, where, note in PLATFORMS[:n]:
        out.append(f"""<div class="card reveal"><span class="badge b-ver">Official site</span>
<h3 style="margin-top:8px">{name}</h3><p class="small"><b>{where}</b></p><p>{note}</p>
<a class="btn btn-sm btn-primary" data-aff="{key}" href="{url}" target="_blank" rel="noopener sponsored">Visit {name} ↗</a></div>""")
    return "".join(out)


HOME_FAQ = [
    ("What does 09911 mean?", "Read as a calendar it spans the festival season: 0 (the start) → 9.9 → 11.11. Read in Mandarin, 9 (jiǔ) sounds like 久 'long-lasting', so 99 means 'forever', and 11 is 'Double Eleven', Singles' Day."),
    ("When is 11.11 in 2026?", "Wednesday 11 November 2026. Most Asian platforms go live at 00:00 UTC+8 (China/Singapore time); many start pre-sales in late October."),
    ("When is the next 9.9 sale?", "9 September every year. In 2027 it falls on a Thursday; the Taobao 99 Mega Sale and Shopee/Lazada 9.9 campaigns usually run from about 1–11 September."),
    ("Is 09911 a store?", "No. 09911 is an independent guide. We don't sell products; we link to official platforms and may earn affiliate commission."),
    ("How do I get alerts?", "Enter your email in any alerts form and pick your platforms. You get a reminder 24 hours before and when each festival goes live."),
]


def index():
    body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">🧧 9.9 → 10.10 → 11.11 → 12.12</span>
    <h1>The world's shopping-festival season, <span class="grad-text">decoded.</span></h1>
    <p class="lead">Countdowns, platform guides, voucher-stacking playbooks and the Chinese number culture behind 9.9 and 11.11. Plan your season once, then save at every festival.</p>
    <div class="cta-row"><a class="btn btn-primary" href="#alerts">🔔 Get free sale alerts</a><a class="btn btn-ghost" href="calendar.html">📅 See the full calendar</a></div>
    <div class="trust-row"><span><b>¥1.695T</b> 2025 Double 11 GMV*</span><span><b>12+</b> festivals tracked</span><span><b>8</b> platforms covered</span></div>
    <p class="small muted" style="margin-top:6px">*Syntun, all platforms, 7 Oct–11 Nov 2025. <a href="stats.html">Sources</a></p>
  </div>
  <div class="countdown-card">
    <div class="cd-label" data-cd-label>Next festival starts in</div>
    <div class="cd-title" data-cd-title>Loading…</div>
    <div class="cd" data-countdown="11-11"><div><b>00</b><span>Days</span></div><div><b>00</b><span>Hrs</span></div><div><b>00</b><span>Min</span></div><div><b>00</b><span>Sec</span></div></div>
    <p class="small" style="color:#ffd9a8;margin:12px 0" data-cd-note></p>
    <div class="chips" data-cd-chips></div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px"><button class="btn btn-gold btn-sm" data-ics="all">+ Add all to my calendar</button><a class="btn btn-sm" style="background:rgba(255,255,255,.1);color:#fff" href="#alerts">Remind me</a></div>
  </div>
</div></section>
{ad("header")}
<section><div class="wrap">
  <div class="section-head"><div><h2>The double-date season at a glance</h2><p>Every month has a mirror date (3.3, 6.6, 9.9…). Four of them move the most money.</p></div><a class="btn btn-ghost btn-sm" href="festivals.html">All festivals →</a></div>
  <div class="grid g4">
    <a class="card reveal" href="9-9.html" style="color:inherit"><span class="badge b-gold">September</span><h3 style="margin-top:8px">9.9 &amp; 99 Mega Sale</h3><p>The season opener in Southeast Asia and China. 九九 sounds like 久久, "forever".</p></a>
    <div class="card reveal"><span class="badge b-soon">October</span><h3 style="margin-top:8px">10.10</h3><p>Mid-season warm-up, plus Double Ninth (Chongyang) and Amazon's October Prime event.</p><a href="calendar.html">Dates →</a></div>
    <a class="card reveal" href="11-11.html" style="color:inherit;border-color:var(--red)"><span class="badge b-live">The big one</span><h3 style="margin-top:8px">11.11 Singles' Day</h3><p>The largest shopping festival on earth by GMV. Now a 4–5 week campaign.</p></a>
    <a class="card reveal" href="festivals.html#s1212" style="color:inherit"><span class="badge b-spon">December</span><h3 style="margin-top:8px">12.12</h3><p>Year-end clearance and gifting, closing the season before Chinese New Year.</p></a>
  </div>
</div></section>
<section class="section-alt"><div class="wrap">
  <div class="section-head"><div><h2>What is your number worth? 🔢</h2><p>Chinese culture reads numbers by sound. Test a phone number, birthday, plate or price.</p></div><a class="btn btn-ghost btn-sm" href="numbers.html">Number library →</a></div>
  <div class="checker" data-checker>
    <div class="form-card">
      <label for="num-input">Enter any number</label>
      <input id="num-input" inputmode="numeric" value="09911" placeholder="e.g. 88168 or 19990911" autocomplete="off">
      <p class="small muted" style="margin-top:10px">Try: <button class="chip" data-try="8888">8888</button> <button class="chip" data-try="1314520">1314520</button> <button class="chip" data-try="4144">4144</button> <button class="chip" data-try="19991111">19991111</button></p>
    </div>
    <div class="form-card" id="num-out" aria-live="polite"></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="section-head"><div><h2>Where to shop the festivals</h2><p>Official platforms only. Each guide covers vouchers, go-live times and what's worth buying.</p></div><a class="btn btn-ghost btn-sm" href="deals.html">Stacking playbook →</a></div>
  <div class="grid g4">{platform_cards(8)}</div>
</div></section>
{lead_box()}
{ad()}
<section class="section-alt"><div class="wrap">
  <div class="section-head"><div><h2>Watch: festival hauls, guides &amp; culture</h2><p>Hand-picked videos. Creators can <a href="careers.html#creators">apply to be featured</a>.</p></div><a class="btn btn-ghost btn-sm" href="videos.html">All videos →</a></div>
  <div class="grid g3" data-videos></div>
</div></section>
<section><div class="wrap grid g3">
  <div class="card reveal"><div class="icon">🏆</div><h3>Monthly giveaway</h3><p>Win vouchers and gadgets. One free entry per person, with bonus entries for sharing.</p><a class="btn btn-sm btn-primary" href="contests.html">Enter now</a></div>
  <div class="card reveal"><div class="icon">📣</div><h3>Brands &amp; sellers</h3><p>Put your festival deal in front of shoppers who are ready to buy. Featured slots, newsletter and video packages.</p><a class="btn btn-sm btn-dark" href="advertise.html">Get featured</a></div>
  <div class="card reveal"><div class="icon">♥</div><h3>Keep 09911 independent</h3><p>No paywalls, no pay-to-rank. Your support funds research, contests and new language editions.</p><a class="btn btn-sm btn-gold" href="donate.html">Support us</a></div>
</div></section>
<section class="section-alt"><div class="wrap" style="max-width:860px">
  <h2 class="center">Frequently asked</h2>{faq_html(HOME_FAQ)}
</div></section>
{ad("footer")}
"""
    return ("index.html", "09911 — 9.9 to 11.11 Festival Calendar, Deals & Lucky Numbers",
            "Countdowns and guides for 9.9, 10.10, 11.11 Singles' Day, 12.12 and 618, plus voucher-stacking tips and the meaning of Chinese lucky numbers.",
            body, faq_ld(HOME_FAQ))


def calendar():
    body = page_hero("Global shopping-festival calendar", "Every double-date sale, Chinese festival and Western mega-sale in one timeline. Go-live times are 00:00 UTC+8 unless noted. Download it to your calendar with built-in reminders.", "Calendar") + f"""
<section style="padding-top:10px"><div class="wrap">
  <div class="chips" style="margin-bottom:16px">
    <button class="chip active" data-tl-filter="all">All</button><button class="chip" data-tl-filter="mega">Mega sales</button>
    <button class="chip" data-tl-filter="sale">Monthly double dates</button><button class="chip" data-tl-filter="culture">Chinese festivals</button>
    <button class="chip" data-ics="all" style="margin-left:auto">⬇ Download .ics (all upcoming)</button>
  </div>
  <ul class="timeline" data-timeline></ul>
  <p class="small muted" style="margin-top:14px">Lunar dates for 2026–2028 are computed from the Chinese calendar. Platforms often open pre-sales 1–3 weeks early; see each festival guide.</p>
</div></section>
{ad()}
<section class="section-alt"><div class="wrap">
  <h2>Best festival by category</h2>
  <div class="table-wrap"><table>
    <tr><th>Category</th><th>Best date</th><th>Why</th></tr>
    <tr><td>Phones &amp; electronics</td><td>11.11 / 618</td><td>Deepest brand-funded subsidies; JD and Tmall compete hardest.</td></tr>
    <tr><td>Fashion &amp; beauty</td><td>11.11 / 9.9</td><td>Brand flagship stores run their biggest gift-with-purchase bundles.</td></tr>
    <tr><td>Home &amp; appliances</td><td>11.11 / 12.12</td><td>Large-item free shipping and installment-plan promotions.</td></tr>
    <tr><td>Groceries &amp; FMCG</td><td>Monthly double dates</td><td>Frequent stack-able vouchers; stock up every month.</td></tr>
    <tr><td>Gifts</td><td>520 · Qixi · 12.12</td><td>Gifting-themed campaigns and bundle discounts.</td></tr>
    <tr><td>Travel</td><td>9.9 / 11.11</td><td>Airline and hotel flash sales ride the same campaigns.</td></tr>
  </table></div>
</div></section>
{lead_box("Get reminded before each date", "Pick the festivals you care about. One email 24 hours before, one when it goes live.", "calendar")}
"""
    return ("calendar.html", "Shopping Festival Calendar 2026–2027: 9.9, 10.10, 11.11, 12.12, 618 | 09911",
            "Full timeline of double-date sales, Chinese festivals and Black Friday with countdowns and downloadable .ics reminders.", body)


NINE_FAQ = [
    ("When is the 9.9 sale?", "9 September every year. Pre-sales often start around 1 September; peak deals drop at 00:00 UTC+8 on the 9th."),
    ("What is the 99 Mega Sale?", "Alibaba's Juhuasuan upgraded its long-running '99' promotion into the 99划算节 in 2019. Overseas it's promoted as the Taobao 99 Mega Sale."),
    ("Why the number 9?", "九 (jiǔ) sounds like 久 (jiǔ), 'long-lasting'. 99 therefore reads as 久久, 'forever', which suits a sale about lasting value."),
    ("Is 9.9 the same as Double Ninth?", "No. 9.9 sales use the solar calendar (9 September). The Double Ninth or Chongyang Festival is the 9th day of the 9th lunar month — 18 October 2026 and 8 October 2027."),
]


def nine():
    body = page_hero("9.9 Super Shopping Day &amp; the 99 Mega Sale", "The opening act of the festival season across Southeast Asia and China — what it is, when it goes live, and how to get the most from it.", "9.9") + f"""
<section style="padding-top:10px"><div class="wrap layout-side">
<article class="prose">
  <h2>What is 9.9?</h2>
  <p>9.9 is a one-day (in practice, about 10-day) mega sale on 9 September. Shopee launched its 9.9 campaign in Southeast Asia in <b>2016</b>. By 2019 it recorded three times the previous year's orders and <b>187,606 items sold per minute</b> (Vulcan Post). In Malaysia in 2025, shoppers saved an estimated <b>RM500 million</b> on 9.9, and Shopee Live drew <b>300 million views</b> on the peak day (Malay Mail).</p>
  <p>In China, Alibaba's Juhuasuan turned its long-running "99" promotion into the <b>99划算节</b> in 2019. It ran with 10-billion-yuan-scale subsidies (百亿补贴) aimed at smaller cities. Overseas it's promoted as the <b>Taobao 99 Mega Sale</b>.</p>
  <h2>Why "9"? The culture behind the date</h2>
  <p>九 (<i>jiǔ</i>) is a homophone of 久 (<i>jiǔ</i>), "long-lasting". Doubled, 九九 becomes 久久: forever. Nine was also the emperor's number: palace doors carry 9×9 rows of golden studs, and couples give 99 or 999 roses to mean "love that lasts". Marketers picked 9.9 to sell <i>lasting value</i>.</p>
  <h2 id="chongyang">Double Ninth (Chongyang 重阳节)</h2>
  <p>The traditional Double Ninth Festival falls on the 9th day of the 9th <i>lunar</i> month (<b>18 Oct 2026, 8 Oct 2027</b>). In the <i>I Ching</i>, nine is the most "yang" number. Customs include climbing hills, chrysanthemum wine, <i>chongyang gao</i> cakes and honouring elders. It is Seniors' Day in China and Taiwan, and Japan marks it as Chōyō on 9 September.</p>
  <h2>9.9 playbook: 6 steps</h2>
  <ol>
    <li><b>Collect vouchers early.</b> Platform, shop and payment vouchers usually open 1–3 days before.</li>
    <li><b>Add to cart on the 8th.</b> Carts don't reserve stock, but checking out is faster.</li>
    <li><b>Be online at 00:00 UTC+8.</b> Flash vouchers run out in minutes.</li>
    <li><b>Stack:</b> platform voucher + shop voucher + free shipping + bank-card promo + cashback portal.</li>
    <li><b>Check price history.</b> Some sellers raise list prices before the sale.</li>
    <li><b>Save the big buys for 11.11</b> if the item is electronics or a large appliance. Discounts usually go deeper then.</li>
  </ol>
  <div class="grid g2" style="margin-top:20px">{platform_cards(4)}</div>
  <h2>FAQ</h2>{faq_html(NINE_FAQ)}
</article>
<aside><div class="toc">
  <div class="countdown-card"><div class="cd-label" data-cd-label>Starts in</div><div class="cd-title" data-cd-title style="font-size:1.1rem">…</div>
  <div class="cd" data-countdown="9-9"><div><b>00</b><span>D</span></div><div><b>00</b><span>H</span></div><div><b>00</b><span>M</span></div><div><b>00</b><span>S</span></div></div><p class="small" style="color:#ffd9a8" data-cd-note></p></div>
  {ad("sidebar")}
  <div class="card"><h3>Selling on 9.9?</h3><p>Get your campaign in front of festival shoppers.</p><a class="btn btn-sm btn-primary" href="advertise.html">Get featured</a></div>
</div></aside>
</div></section>
{lead_box("Get the 9.9 go-live alert", "We'll email you 24 hours before and when the 9.9 and 99 Mega Sale vouchers drop.", "9-9")}
"""
    return ("9-9.html", "9.9 Sale & Taobao 99 Mega Sale Guide — Dates, Tips, Meaning | 09911",
            "Everything about the 9.9 Super Shopping Day and 99 Mega Sale: history, go-live times, voucher stacking and why 99 means 'forever' in Chinese.",
            body, faq_ld(NINE_FAQ))


ELEVEN_FAQ = [
    ("When is 11.11 in 2026?", "Wednesday 11 November 2026. Chinese platforms now start pre-sales in mid-October; the final peak is 00:00 UTC+8 on 11 November."),
    ("How big is Singles' Day?", "Alibaba's last published figure was ¥540.3B (US$84.5B) in 2021. Syntun estimates ¥1.695 trillion (~US$238B) across all platforms for 7 Oct–11 Nov 2025."),
    ("Why is it called Singles' Day?", "It started in 1993 as an 'anti-Valentine's' day among Nanjing University students: four 1s look like four 'bare sticks' (光棍), slang for single people. Alibaba turned it into a sale in 2009."),
    ("Can I shop 11.11 outside China?", "Yes. AliExpress, Lazada, Shopee, TikTok Shop and many global retailers run 11.11 campaigns with international shipping."),
]


def eleven():
    body = page_hero("11.11 Singles' Day: the complete guide", "The world's largest shopping festival: its history, dates, how the pre-sale works, and a stacking strategy that holds up.", "11.11") + f"""
<section style="padding-top:10px"><div class="wrap layout-side">
<article class="prose">
  <h2>From bachelor joke to trillion-yuan festival</h2>
  <p>Singles' Day (光棍节, <i>Guānggùn Jié</i>) began in <b>1993</b> among Nanjing University students. The date 11/11 is four "bare sticks", slang for singles. In <b>2009</b>, Alibaba ran the first 11.11 sale with 27 brands and about US$7.8M in sales. By <b>2021</b>, Alibaba's own GMV reached <b>¥540.3 billion (US$84.5B)</b>, after which it stopped publishing a headline number.</p>
  <p>The festival has since spread across platforms and weeks. Syntun's 2025 report puts all-platform GMV at <b>¥1.695 trillion (~US$238B)</b> for 7 Oct–11 Nov 2025, including ¥1,619.1B on e-commerce platforms and ¥67B via instant retail. <a href="stats.html">See the full stats →</a></p>
  <h2>How the modern 11.11 works</h2>
  <div class="table-wrap"><table>
    <tr><th>Phase</th><th>Typical timing</th><th>What to do</th></tr>
    <tr><td>Pre-sale / deposits</td><td>Mid–late October</td><td>Pay a small deposit to lock a discounted final price.</td></tr>
    <tr><td>Wave 1</td><td>Late Oct – early Nov</td><td>First voucher drops; compare prices and add to cart.</td></tr>
    <tr><td>Warm-up</td><td>1–10 November</td><td>Collect platform and shop vouchers; do the cross-store discount maths.</td></tr>
    <tr><td>Peak</td><td>11 Nov, 00:00–02:00 UTC+8</td><td>Flash vouchers and doorbusters. Check out fast.</td></tr>
    <tr><td>Returns window</td><td>After the festival</td><td>Check price-protection policies if prices drop.</td></tr>
  </table></div>
  <h2>The four-layer stacking method</h2>
  <ol>
    <li><b>Platform layer:</b> sitewide vouchers and cross-store "spend X save Y" offers.</li>
    <li><b>Store layer:</b> follow the shop to unlock follower coupons.</li>
    <li><b>Payment layer:</b> bank-card and e-wallet cashback (often capped; read the caps).</li>
    <li><b>Portal layer:</b> cashback sites and coins or points.</li>
  </ol>
  <p class="small muted">Tip: work out the <i>effective</i> price after all layers and compare it with the 30-day low, not the list price.</p>
  <h2>What's worth buying on 11.11</h2>
  <ul class="pill-list"><li>Flagship phones</li><li>Laptops &amp; tablets</li><li>Large appliances</li><li>Skincare sets</li><li>Winter apparel</li><li>Smart-home kits</li><li>Luggage</li><li>Pantry stock-ups</li></ul>
  <div class="grid g2" style="margin-top:20px">{platform_cards(4)}</div>
  <h2>FAQ</h2>{faq_html(ELEVEN_FAQ)}
</article>
<aside><div class="toc">
  <div class="countdown-card"><div class="cd-label" data-cd-label>Starts in</div><div class="cd-title" data-cd-title style="font-size:1.1rem">…</div>
  <div class="cd" data-countdown="11-11"><div><b>00</b><span>D</span></div><div><b>00</b><span>H</span></div><div><b>00</b><span>M</span></div><div><b>00</b><span>S</span></div></div><p class="small" style="color:#ffd9a8" data-cd-note></p></div>
  {ad("sidebar")}
  <div class="card"><h3>🏆 11.11 Giveaway</h3><p>Enter free to win festival vouchers.</p><a class="btn btn-sm btn-gold" href="contests.html">Enter</a></div>
</div></aside>
</div></section>
{lead_box("Be first when 11.11 goes live", "Pre-sale opening, wave-1 vouchers and the midnight peak: three emails, all useful.", "11-11")}
"""
    return ("11-11.html", "11.11 Singles' Day 2026 Guide — Dates, GMV, Stacking Strategy | 09911",
            "Singles' Day explained: history since 1993, 2025 GMV of ¥1.695 trillion, pre-sale timeline and the four-layer voucher stacking method.",
            body, faq_ld(ELEVEN_FAQ))


def festivals():
    items = [
        ("s33", "3.3 → 8.8 monthly double dates", "Shopee, Lazada and TikTok Shop run a sale on every mirror date. Smaller than the big four, but good for groceries and restocks."),
        ("s618", "618 Mid-Year Festival", "Anchored by JD.com's founding anniversary (18 June). China's second-largest shopping festival, strongest in electronics and appliances."),
        ("s520", "520 &amp; Qixi", "5-2-0 sounds like 我爱你, 'I love you'. With Qixi (the 7th day of the 7th lunar month), it drives gifting, jewellery and flowers."),
        ("s99", "9.9 &amp; 99 Mega Sale", "The season opener. <a href='9-9.html'>Full guide →</a>"),
        ("s1010", "10.10", "Mid-season sale, often themed around brands or payday. Watch for early 11.11 pre-sale teasers."),
        ("s1111", "11.11 Singles' Day", "The largest shopping festival in the world. <a href='11-11.html'>Full guide →</a>"),
        ("sbf", "Black Friday &amp; Cyber Monday", "The 4th Friday of November and the Monday after. Global platforms run parallel campaigns; good for Western brands."),
        ("s1212", "12.12 Year-End Sale", "Started by Taobao in 2011. Now the year-end sale across Southeast Asia: clearance stock, gifts and free-shipping marathons."),
        ("scny", "Chinese New Year &amp; Dragon Boat", "Pre-CNY sales end before logistics pause for the holiday. Order 2–3 weeks early. The Dragon Boat Festival is the 5th day of the 5th lunar month."),
        ("smid", "Mid-Autumn Festival", "Mooncakes, lanterns and family gifting on the 15th day of the 8th lunar month."),
        ("sqixi", "Qixi Festival", "Chinese Valentine's Day, the 7th day of the 7th lunar month."),
    ]
    cards = "".join(f'<div class="card reveal" id="{i}"><h3>{t}</h3><p>{d}</p><button class="btn btn-sm btn-ghost" onclick="location.href=\'calendar.html\'">See dates</button></div>' for i, t, d in items)
    body = page_hero("Every shopping festival, explained", "The global calendar of double dates, Chinese cultural festivals and Western mega-sales, and what each one is best for.", "Festivals") + f"""
<section style="padding-top:10px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
{ad()}
{lead_box()}
"""
    return ("festivals.html", "All Shopping Festivals Explained: 618, 9.9, 11.11, 12.12, 520, CNY | 09911",
            "Guide to double-date sales, 618, 520, Qixi, Chinese New Year, Black Friday and 12.12: what each festival is and what to buy.", body)


def deals():
    body = page_hero("Platforms, vouchers &amp; the stacking playbook", "Where to shop each festival, how to stack every discount layer, and how to share a deal with the community.", "Deals") + f"""
<section style="padding-top:10px"><div class="wrap">
  <div class="grid g4">{platform_cards(8)}</div>
  <p class="small muted" style="margin-top:10px">Links go to official platform homepages. Some may be affiliate links (<a href="legal.html#affiliate">disclosure</a>). We never publish invented prices. Live deals are checked by editors before they are posted.</p>
</div></section>
{ad()}
<section class="section-alt"><div class="wrap">
  <h2>Stacking calculator</h2>
  <div class="checker">
    <div class="form-card" id="stack">
      <div class="row"><div><label for="p0">List price</label><input id="p0" type="number" value="200" min="0"></div><div><label for="p1">Platform voucher (off)</label><input id="p1" type="number" value="20" min="0"></div></div>
      <div class="row"><div><label for="p2">Shop voucher (off)</label><input id="p2" type="number" value="10" min="0"></div><div><label for="p3">Bank / wallet cashback %</label><input id="p3" type="number" value="5" min="0" max="100"></div></div>
      <div class="row"><div><label for="p4">Cashback portal %</label><input id="p4" type="number" value="3" min="0" max="100"></div><div><label for="p5">30-day lowest price</label><input id="p5" type="number" value="175" min="0"></div></div>
    </div>
    <div class="form-card"><h3>Effective price</h3><div class="stat" id="s-out">—</div><p id="s-note" class="muted"></p></div>
  </div>
  <script>
  (function(){{var ids=["p0","p1","p2","p3","p4","p5"];function g(i){{return +document.getElementById(i).value||0}}
  function run(){{var a=Math.max(0,g("p0")-g("p1")-g("p2"));var e=a*(1-g("p3")/100)*(1-g("p4")/100);var low=g("p5");
  document.getElementById("s-out").textContent=e.toFixed(2);var off=g("p0")?((1-e/g("p0"))*100).toFixed(1):0;
  document.getElementById("s-note").innerHTML="Total saving <b>"+off+"%</b> vs list. "+(low?(e<low?"✅ Beats the 30-day low by "+(low-e).toFixed(2):"⚠️ Not better than the 30-day low: wait or skip."):"");}}
  ids.forEach(function(i){{document.getElementById(i).addEventListener("input",run)}});run();}})();
  </script>
</div></section>
<section id="submit"><div class="wrap grid g2">
  <div><h2>Submit a deal or voucher</h2><p class="muted">Found a great festival deal? Send it in. Editors check every submission (link, price and expiry) before it's published. Top submitters each month get bonus <a href="contests.html">giveaway</a> entries.</p>
  <ul><li>Official store links only</li><li>Include the voucher code and expiry</li><li>Tell us the country or region</li></ul></div>
  <form class="form-card" data-form="Deal Submission" data-ok="Thanks! Our editors will verify your deal within 24 hours.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="d-name">Your name</label><input id="d-name" name="name" required></div><div><label for="d-email">Email</label><input id="d-email" type="email" name="email" required></div></div>
    <label for="d-url">Deal URL</label><input id="d-url" type="url" name="deal_url" required placeholder="https://">
    <div class="row"><div><label for="d-plat">Platform</label><select id="d-plat" name="platform"><option>Shopee</option><option>Lazada</option><option>AliExpress</option><option>Taobao/Tmall</option><option>JD.com</option><option>Amazon</option><option>TikTok Shop</option><option>Temu</option><option>Other</option></select></div>
    <div><label for="d-code">Voucher code (optional)</label><input id="d-code" name="code"></div></div>
    <div class="row"><div><label for="d-country">Country</label><input id="d-country" name="country"></div><div><label for="d-exp">Expires</label><input id="d-exp" type="date" name="expires"></div></div>
    <label for="d-desc">Why is it a good deal?</label><textarea id="d-desc" name="details" required></textarea>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Submit deal</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
{lead_box()}
"""
    return ("deals.html", "Festival Platforms, Voucher Stacking Calculator & Deal Submission | 09911",
            "Official platform guides for Shopee, Lazada, AliExpress, Taobao, JD, Amazon and TikTok Shop, a voucher stacking calculator, and a deal submission form.", body)


NUMS = [
    ("0", "零", "líng", "Wholeness and new beginnings. In internet slang 0 can stand for 你 ('you'), as in 0564 or 0748.", "neutral"),
    ("1", "一", "yī / yāo", "Unity and being first. On phones it's read 'yāo', which echoes 要, 'want'.", "neutral"),
    ("2", "二", "èr", "'Good things come in pairs' (好事成双). Weddings use doubled characters (囍).", "lucky"),
    ("3", "三", "sān", "Sounds like 生 (life, birth). Also like 散 (scatter), so gifts in threes are sometimes avoided.", "mixed"),
    ("4", "四", "sì", "Sounds like 死 (death). Many buildings skip 4th, 14th and 24th floors.", "unlucky"),
    ("5", "五", "wǔ", "The Five Elements (五行). As slang, 5 = 我 ('I'), as in 520.", "neutral"),
    ("6", "六", "liù", "Sounds like 流 (flow): things go smoothly. '666' means 'awesome' online.", "lucky"),
    ("7", "七", "qī", "Togetherness (起) and Qixi love day, but the 7th lunar month is Ghost Month.", "mixed"),
    ("8", "八", "bā", "Sounds like 发 (fā, prosper). Beijing opened the 2008 Olympics at 8:08:08 pm on 8/8/08.", "lucky"),
    ("9", "九", "jiǔ", "Sounds like 久 ('long-lasting'). The emperor's number, and the root of 99 = 'forever'.", "lucky"),
    ("11", "十一", "shíyī", "'Double Eleven': four 'bare sticks' on 11/11 gave us Singles' Day. 十一 is also National Day (1 Oct).", "neutral"),
    ("99", "九十九 / 九九", "jiǔshíjiǔ", "久久: forever. 99 roses means eternal love; it's also the 9.9 festival.", "lucky"),
    ("520", "五二零", "wǔ èr líng", "我爱你, 'I love you'. 20 May is online Valentine's Day.", "lucky"),
    ("1314", "一三一四", "yī sān yī sì", "一生一世, 'for a lifetime'. Paired with 520 as 5201314.", "lucky"),
    ("168", "一六八", "yāo liù bā", "一路发, 'prosper all the way'. A favourite for shop numbers and plates.", "lucky"),
    ("888", "八八八", "bā bā bā", "Triple prosperity; commands premium prices on plates and phone numbers.", "lucky"),
    ("250", "二百五", "èrbǎiwǔ", "Slang for a fool. Avoid it in prices and gift amounts.", "unlucky"),
    ("09911", "零九九一一", "líng jiǔ jiǔ yāo yāo", "Our name: the festival season (0 → 9.9 → 11.11), with 久久 'forever' in the middle.", "lucky"),
]


def numbers():
    cards = "".join(
        f"""<div class="card num-card reveal" id="n{n}"><span class="badge {'b-ver' if k=='lucky' else 'b-hot' if k=='unlucky' else 'b-gold'}">{k}</span>
<div style="margin-top:8px"><span class="big">{n}</span><span class="han">{h}</span></div><p class="small"><i>{p}</i></p><p>{m}</p></div>"""
        for n, h, p, m, k in NUMS)
    faq = [("Why is 8 lucky in Chinese?", "八 (bā) sounds like 发 (fā), 'to prosper'. That's why 8s raise the price of phone numbers, plates and addresses."),
           ("Why is 4 unlucky?", "四 (sì) sounds like 死 (sǐ), 'death'. Hospitals and buildings often skip floors with 4."),
           ("What does 99 mean?", "九九 sounds like 久久, 'forever'. It's used in love and longevity contexts and gives its name to the 9.9 festival."),
           ("What does 520 mean?", "五二零 sounds like 我爱你, 'I love you'. 20 May is celebrated as online Valentine's Day.")]
    body = page_hero("Chinese lucky numbers: meanings &amp; checker", "How Mandarin homophones make numbers lucky or unlucky, and what that means for dates, prices, phone numbers and domain names.", "Lucky Numbers") + f"""
<section style="padding-top:10px"><div class="wrap">
  <div class="checker" data-checker>
    <div class="form-card"><label for="num-input">Check any number</label><input id="num-input" inputmode="numeric" value="09911" autocomplete="off">
    <p class="small muted" style="margin-top:10px">Try: <button class="chip" data-try="168">168</button> <button class="chip" data-try="5201314">5201314</button> <button class="chip" data-try="14">14</button> <button class="chip" data-try="88888">88888</button></p>
    <p class="small">Want a full written reading for a business name, phone or plate? <a href="#reading">Request one below</a>.</p></div>
    <div class="form-card" id="num-out" aria-live="polite"></div>
  </div>
</div></section>
{ad()}
<section class="section-alt"><div class="wrap"><h2>The number library</h2><div class="grid g3">{cards}</div></div></section>
<section id="reading"><div class="wrap grid g2">
  <div><h2>Number reading for your business</h2><p class="muted">Launching in Chinese-speaking markets? We check brand numbers, prices, phone numbers and launch dates for unfortunate homophones, and suggest auspicious alternatives.</p>
  <ul><li>Price-point review (e.g. ¥88, ¥168, ¥520)</li><li>Launch-date selection around festivals</li><li>Phone and plate number review</li><li>Domain and brand-number review</li></ul></div>
  <form class="form-card" data-form="Number Reading Request" data-ok="Thanks! We'll reply with a quote and turnaround time.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="r-n">Name</label><input id="r-n" name="name" required></div><div><label for="r-e">Email</label><input id="r-e" type="email" name="email" required></div></div>
    <label for="r-t">What should we review?</label><select id="r-t" name="type"><option>Business price points</option><option>Launch date</option><option>Phone / plate number</option><option>Domain / brand number</option><option>Other</option></select>
    <label for="r-d">Numbers &amp; context</label><textarea id="r-d" name="details" required></textarea>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Request a reading</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
<section class="section-alt"><div class="wrap" style="max-width:860px"><h2>FAQ</h2>{faq_html(faq)}</div></section>
{lead_box()}
"""
    return ("numbers.html", "Chinese Lucky Numbers Meaning: 8, 9, 99, 520, 1314, 168 + Free Checker | 09911",
            "Meanings of Chinese lucky and unlucky numbers (0–9, 11, 99, 520, 1314, 168, 888) with a free interactive number luck checker.", body, faq_ld(faq))


PAGES_A = [index(), calendar(), nine(), eleven(), festivals(), deals(), numbers()]
