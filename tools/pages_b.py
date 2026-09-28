from partials import ad, lead_box, page_hero, faq_ld, faq_html, CONTACT

GMV = [(2009, 0.05), (2010, 0.94), (2011, 5.2), (2012, 19.1), (2013, 35.0), (2014, 57.1), (2015, 91.2), (2016, 120.7),
       (2017, 168.2), (2018, 213.5), (2019, 268.4), (2020, 498.2), (2021, 540.3)]


def stats():
    mx = max(v for _, v in GMV)
    bars = "".join(f'<div class="bar"><span>{y}</span><div class="track"><div class="fill" data-w="{max(0.6, v / mx * 100):.1f}"></div></div><b>¥{v:g}B</b></div>' for y, v in GMV)
    body = page_hero("Shopping-festival statistics", "The numbers behind 11.11, 9.9 and the double-date economy, each with its source.", "Stats") + f"""
<section style="padding-top:10px"><div class="wrap grid g4">
  <div class="card"><div class="stat">¥1.695T</div><p>All-platform Double 11 GMV, 7 Oct–11 Nov 2025 (~US$238B), per Syntun.</p></div>
  <div class="card"><div class="stat">¥540.3B</div><p>Alibaba's last published 11.11 GMV (2021), equal to US$84.5B.</p></div>
  <div class="card"><div class="stat">187,606</div><p>Items sold per minute on Shopee 9.9 in 2019 (Vulcan Post).</p></div>
  <div class="card"><div class="stat">RM500M+</div><p>Estimated savings by Malaysian shoppers on Shopee 9.9, 2025 (Malay Mail).</p></div>
</div></section>
<section class="section-alt"><div class="wrap">
  <h2>Alibaba 11.11 GMV, 2009–2021 (¥ billions)</h2>
  <p class="muted small">Official Alibaba figures. From 2020 the event window grew from one day to 11 days (1–11 Nov), so 2020–21 aren't like-for-like with earlier years. Alibaba stopped publishing GMV after 2021.</p>
  <div class="bars" role="img" aria-label="Bar chart of Alibaba Singles Day GMV by year">{bars}</div>
</div></section>
<section><div class="wrap">
  <h2>All-platform Double 11 (Syntun estimates)</h2>
  <div class="table-wrap"><table>
    <tr><th>Year</th><th>GMV (¥)</th><th>Notes</th></tr>
    <tr><td>2023</td><td>≈ ¥1.14 trillion</td><td>All platforms, multi-week window</td></tr>
    <tr><td>2024</td><td>≈ ¥1.44 trillion (≈ US$202.8B, +26.6%)</td><td>Longest festival window to date</td></tr>
    <tr><td>2025</td><td>¥1.695 trillion (~US$238B)</td><td>7 Oct–11 Nov; e-commerce ¥1,619.1B, instant retail ¥67B, community group-buying ¥9B</td></tr>
  </table></div>
  <p class="small muted" style="margin-top:10px">Windows differ between years; treat year-on-year growth as indicative only.</p>
  <h3 style="margin-top:28px">Sources</h3>
  <ul class="small">
    <li><a href="https://www.prnewswire.com/news-releases/syntun--2025-double-11-promotion-report-the-gmv-during-china-double-11-shopping-festival-reached-1695-billion-cny-238-billion-usd-302613127.html" target="_blank" rel="noopener">Syntun 2025 Double 11 report (PR Newswire)</a></li>
    <li><a href="https://www.aljazeera.com/economy/2021/11/12/chinas-singles-day-posts-record-sales-of-84-5bn" target="_blank" rel="noopener">Al Jazeera: Singles' Day 2021 record $84.5bn</a></li>
    <li><a href="https://queue-it.com/blog/singles-day-statistics/" target="_blank" rel="noopener">Queue-it: Singles' Day statistics</a></li>
    <li><a href="https://vulcanpost.com/712334/shopee-pioneer-9-9-sale-singapore/" target="_blank" rel="noopener">Vulcan Post: Shopee pioneered 9.9</a></li>
    <li><a href="https://www.malaymail.com/news/money/mediaoutreach/2025/09/11/malaysians-enjoyed-rm500-million-savings-14x-faster-delivery-on-shopee-99-super-shopping-day/408739" target="_blank" rel="noopener">Malay Mail: Shopee 9.9 Malaysia 2025</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Double_Ninth_Festival" target="_blank" rel="noopener">Wikipedia: Double Ninth Festival</a></li>
  </ul>
  <p><button class="btn btn-ghost btn-sm" data-share>Share these stats</button></p>
</div></section>
{ad()}
{lead_box("Get the 11.11 results the day they land", "Our post-festival GMV breakdown, platform by platform, in your inbox.", "stats")}
"""
    return ("stats.html", "Singles' Day & 9.9 Statistics: GMV 2009–2025 with Sources | 09911",
            "Double 11 GMV history from ¥0.05B in 2009 to ¥1.695 trillion in 2025, plus Shopee 9.9 records. Every figure is sourced.", body)


def videos():
    body = page_hero("Videos: hauls, guides &amp; culture", "Festival hauls, voucher-stacking tutorials and the cultural stories behind the numbers.", "Videos") + f"""
<section style="padding-top:10px"><div class="wrap"><div class="grid g3" data-videos></div>
<p class="center" style="margin-top:20px"><a class="btn btn-primary" href="https://www.youtube.com/" target="_blank" rel="noopener" id="yt-sub">▶ Subscribe on YouTube</a></p></div></section>
<script>addEventListener("DOMContentLoaded",function(){{document.getElementById("yt-sub").href=(window.SITE_CONFIG||{{}}).YOUTUBE_CHANNEL_URL||"https://www.youtube.com/";}});</script>
{ad()}
<section class="section-alt" id="submit-video"><div class="wrap grid g2">
  <div><h2>Creators: get featured</h2><p class="muted">Do you make haul, unboxing, deal or Chinese-culture videos? Submit one to be embedded on 09911 and shared in our newsletter. Paid collaborations are available for festival campaigns.</p></div>
  <form class="form-card" data-form="Video Submission" data-ok="Thanks! We'll review your video and get back to you.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="v-n">Channel name</label><input id="v-n" name="name" required></div><div><label for="v-e">Email</label><input id="v-e" type="email" name="email" required></div></div>
    <label for="v-u">Video URL</label><input id="v-u" type="url" name="video_url" required placeholder="https://youtube.com/watch?v=">
    <label for="v-s">Subscribers</label><select id="v-s" name="subscribers"><option>&lt;1K</option><option>1K–10K</option><option>10K–100K</option><option>100K–1M</option><option>1M+</option></select>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Submit video</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
"""
    return ("videos.html", "Festival Shopping Videos: 11.11 Hauls, Voucher Guides, Chinese Culture | 09911",
            "Curated videos on 11.11 and 9.9 hauls, voucher stacking tutorials and Chinese lucky-number culture. Creators can submit videos.", body)


def contests():
    rules = [("Who can enter?", "Anyone aged 18+ (or the age of majority where you live), in any country where the promotion is lawful. Void where prohibited."),
             ("Do I have to buy anything?", "No. No purchase or payment is necessary to enter or win, and purchasing does not improve your chances."),
             ("How are winners chosen?", "By random draw from all valid entries after the closing date. Winners are notified by email and have 7 days to claim."),
             ("Can I enter more than once?", "One entry per person per contest. Duplicate or automated entries are disqualified."),
             ("How is the prize delivered?", "As a digital voucher or gift card of equivalent value, chosen from the platforms we cover and subject to availability in your region.")]
    body = page_hero("Contests, giveaways &amp; prizes", "Free to enter, drawn at random and paid out in platform vouchers. One entry per person per contest.", "Contests") + f"""
<section style="padding-top:10px"><div class="wrap grid g3">
  <div class="card tier featured"><span class="ribbon">OPEN</span><div class="icon">🏆</div><h3>11.11 Festival Giveaway</h3><p class="price">$99 + $11 + $11</p><ul><li>3 winners, drawn at random</li><li>Closes 11 Nov, 23:59 UTC+8</li><li>Prize as vouchers for a platform of the winner's choice</li></ul><a class="btn btn-primary" href="#enter">Enter free</a></div>
  <div class="card tier"><div class="icon">🎥</div><h3>Creator Challenge</h3><p class="price">Featured + cash</p><ul><li>Best "how I stacked 11.11" video</li><li>Judged on usefulness and clarity</li><li>Winner featured on the homepage</li></ul><a class="btn btn-ghost" href="videos.html#submit-video">Submit video</a></div>
  <div class="card tier"><div class="icon">🔎</div><h3>Deal Hunter of the Month</h3><p class="price">Badge + bonus</p><ul><li>Most verified deal submissions</li><li>Bonus giveaway entries</li><li>Profile shout-out in the newsletter</li></ul><a class="btn btn-ghost" href="deals.html#submit">Submit deals</a></div>
</div></section>
<section class="section-alt" id="enter"><div class="wrap grid g2">
  <div><h2>Enter the current giveaway</h2><p class="muted">Takes 20 seconds. We'll email you if you win.</p>
  <p class="small">Want to sponsor a prize? Brands that fund prizes get logo placement, newsletter mentions and social posts. <a href="advertise.html#partner">Sponsor a contest →</a></p></div>
  <form class="form-card" data-form="Contest Entry — 11.11 Giveaway" data-ok="You're entered! Good luck 🍀 Winners are notified by email.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="c-n">Full name</label><input id="c-n" name="name" required></div><div><label for="c-e">Email</label><input id="c-e" type="email" name="email" required></div></div>
    <div class="row"><div><label for="c-c">Country</label><input id="c-c" name="country" required></div><div><label for="c-p">Preferred platform</label><select id="c-p" name="platform"><option>Shopee</option><option>Lazada</option><option>AliExpress</option><option>Amazon</option><option>Other</option></select></div></div>
    <label for="c-q">Skill question: what does 九九 (99) sound like in Chinese?</label>
    <select id="c-q" name="answer" required><option value="">Choose…</option><option>久久 — forever</option><option>酒酒 — wine wine</option><option>救救 — help help</option></select>
    <label class="check" style="margin-top:10px"><input type="checkbox" name="age18" value="yes" required> I am 18+ and accept the contest rules below.</label>
    <label class="check"><input type="checkbox" name="newsletter" value="yes"> Also send me festival alerts (optional).</label>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Enter giveaway</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
<section><div class="wrap" style="max-width:860px"><h2>Official rules (summary)</h2>{faq_html(rules)}
<p class="small muted">The sponsor is the operator of 09911.com. This promotion is not sponsored, endorsed or administered by, or associated with, any platform named. Full terms: <a href="legal.html#terms">Terms</a>.</p></div></section>
"""
    return ("contests.html", "Contests & Giveaways — Win Festival Vouchers | 09911",
            "Free-to-enter giveaways for 11.11 and other shopping festivals, a creator challenge and Deal Hunter of the Month. No purchase necessary.", body, faq_ld(rules))


def advertise():
    faq = [("Who visits 09911?", "Shoppers planning festival purchases across Southeast Asia, China-curious global buyers and diaspora audiences. Visitors arrive with high purchase intent in the weeks before each festival."),
           ("How are sponsored placements labelled?", "Always clearly marked 'Sponsored'. Editorial guides are never for sale; placements are."),
           ("What do you need from me?", "Your offer, landing URL, voucher codes (if any), logo and the festival window. We handle design and copy."),
           ("Can I buy or partner on the 09911.com domain itself?", f"Yes. Serious enquiries about acquisition, joint ventures or white-label use go through <a href='{CONTACT}'>web.works/contact</a>.")]
    body = page_hero("Advertise, sponsor or partner with 09911", "Reach shoppers when they're ready to buy: in the weeks before 9.9, 11.11 and 12.12.", "Advertise") + f"""
<section style="padding-top:10px"><div class="wrap grid g4">
  <div class="card"><div class="icon">🎯</div><h3>High intent</h3><p>Visitors arrive to plan purchases, not to browse.</p></div>
  <div class="card"><div class="icon">⏱</div><h3>Timed to festivals</h3><p>Your offer goes live with the countdown and alert emails.</p></div>
  <div class="card"><div class="icon">🌏</div><h3>Asia + global</h3><p>SEA, Greater China, diaspora and cross-border shoppers.</p></div>
  <div class="card"><div class="icon">📊</div><h3>Transparent reporting</h3><p>Clicks, impressions and leads reported after every campaign.</p></div>
</div></section>
<section class="section-alt"><div class="wrap">
  <div class="section-head"><div><h2>Packages</h2><p>Launch pricing (USD). Custom bundles are available.</p></div></div>
  <div class="grid g4">
    <div class="card tier"><h3>Featured Deal</h3><div class="price">$49<span class="small muted">/week</span></div><ul><li>Sponsored card on Deals and the festival page</li><li>"Sponsored" badge</li><li>UTM click report</li></ul><a class="btn btn-ghost" href="#lead" data-pkg="Featured Deal">Choose</a></div>
    <div class="card tier featured"><span class="ribbon">MOST POPULAR</span><h3>Festival Takeover</h3><div class="price">$499<span class="small muted">/festival</span></div><ul><li>Countdown-card branding</li><li>Homepage hero slot</li><li>Dedicated alert email</li><li>Contest prize sponsorship</li></ul><a class="btn btn-primary" href="#lead" data-pkg="Festival Takeover">Choose</a></div>
    <div class="card tier"><h3>Newsletter &amp; Video</h3><div class="price">$199</div><ul><li>Newsletter feature</li><li>60-second video integration</li><li>Social cross-post</li></ul><a class="btn btn-ghost" href="#lead" data-pkg="Newsletter & Video">Choose</a></div>
    <div class="card tier" id="partner"><h3>Title Partner</h3><div class="price">Custom</div><ul><li>"Presented by" across the season</li><li>Co-branded calendar and guides</li><li>Domain partnership or white-label</li></ul><a class="btn btn-dark" href="#lead" data-pkg="Title Partner / Domain">Talk to us</a></div>
  </div>
</div></section>
<section id="lead"><div class="wrap grid g2">
  <div>
    <span class="eyebrow">Reply within 1 business day</span>
    <h2 style="margin-top:12px">Get your media kit &amp; quote</h2>
    <p class="muted">Tell us what you're promoting. You'll get availability, a proposal and next steps.</p>
    <ol class="muted"><li>Send the form (about 60 seconds)</li><li>Receive a proposal and media kit</li><li>Approve the creative, then go live with the festival</li></ol>
    <div class="card" style="margin-top:16px"><b>Interested in the domain itself?</b><p class="small">Acquisition, investment and joint-venture enquiries for 09911.com:</p><a class="btn btn-gold btn-sm" href="{CONTACT}" target="_blank" rel="noopener">Contact the owner ↗</a></div>
  </div>
  <form class="form-card" data-form="Advertising / Partnership Lead" data-ok="Thank you! Your media kit and proposal are on the way. Expect a reply within 1 business day.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <label>I'm interested in</label>
    <div class="seg" id="pkg-seg">
      <label><input type="radio" name="interest" value="Featured Deal" required><span>Featured deal</span></label>
      <label><input type="radio" name="interest" value="Festival Takeover"><span>Festival takeover</span></label>
      <label><input type="radio" name="interest" value="Newsletter & Video"><span>Newsletter/video</span></label>
      <label><input type="radio" name="interest" value="Sponsorship"><span>Sponsorship</span></label>
      <label><input type="radio" name="interest" value="Title Partner / Domain"><span>Partnership/domain</span></label>
    </div>
    <div class="row"><div><label for="a-n">Name</label><input id="a-n" name="name" required autocomplete="name"></div><div><label for="a-e">Work email</label><input id="a-e" type="email" name="email" required autocomplete="email"></div></div>
    <div class="row"><div><label for="a-c">Company / store</label><input id="a-c" name="company" required></div><div><label for="a-w">Website</label><input id="a-w" type="url" name="website" placeholder="https://"></div></div>
    <div class="row"><div><label for="a-f">Festival</label><select id="a-f" name="festival"><option>11.11</option><option>12.12</option><option>9.9 (next year)</option><option>618</option><option>Chinese New Year</option><option>Always-on</option></select></div>
    <div><label for="a-b">Budget (USD)</label><select id="a-b" name="budget"><option>&lt; $250</option><option>$250–1,000</option><option>$1,000–5,000</option><option>$5,000+</option><option>Not sure yet</option></select></div></div>
    <label for="a-m">Goals / message</label><textarea id="a-m" name="message" placeholder="What are you promoting, and to whom?"></textarea>
    <label class="check" style="margin-top:10px"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this enquiry.</label>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Send &amp; get media kit →</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
<script>document.querySelectorAll("[data-pkg]").forEach(function(a){{a.addEventListener("click",function(){{var v=a.getAttribute("data-pkg");document.querySelectorAll("#pkg-seg input").forEach(function(i){{if(i.value===v)i.checked=true}})}})}});</script>
<section class="section-alt"><div class="wrap" style="max-width:860px"><h2>FAQ</h2>{faq_html(faq)}</div></section>
"""
    return ("advertise.html", "Advertise, Sponsor or Partner — Reach Festival Shoppers | 09911",
            "Featured deals, festival takeovers, newsletter and video sponsorships, contest sponsorship and domain partnerships on 09911.com.", body, faq_ld(faq))


def donate():
    body = page_hero("Support 09911", "Keep the guides free, independent and ad-light. Every contribution is spent openly on the items below.", "Donate") + f"""
<section style="padding-top:10px"><div class="wrap grid g4">
  <div class="card tier"><h3>Lucky 9</h3><div class="price">$9</div><ul><li>Name on the supporters wall</li><li>Our thanks, in 9 languages</li></ul><a class="btn btn-ghost" data-donate="buymeacoffee" href="#pledge">Give $9</a></div>
  <div class="card tier"><h3>Double Nine</h3><div class="price">$19</div><ul><li>Supporter badge</li><li>Early festival guides</li></ul><a class="btn btn-ghost" data-donate="kofi" href="#pledge">Give $19</a></div>
  <div class="card tier featured"><span class="ribbon">久久 FOREVER</span><h3>Forever (99)</h3><div class="price">$99</div><ul><li>Everything above</li><li>Bonus giveaway entries</li><li>Thank-you in the 11.11 recap</li></ul><a class="btn btn-primary" data-donate="paypal" href="#pledge">Give $99</a></div>
  <div class="card tier"><h3>Monthly patron</h3><div class="price">Any</div><ul><li>Recurring support</li><li>Vote on new features</li></ul><a class="btn btn-ghost" data-donate="github_sponsors" href="#pledge">Become a patron</a></div>
</div></section>
<section class="section-alt"><div class="wrap">
  <h2>Where your support goes</h2>
  <div class="bars">
    <div class="bar"><span>Ops</span><div class="track"><div class="fill" data-w="30"></div></div><b>30%</b></div>
    <div class="bar"><span>Talent</span><div class="track"><div class="fill" data-w="25"></div></div><b>25%</b></div>
    <div class="bar"><span>Prizes</span><div class="track"><div class="fill" data-w="20"></div></div><b>20%</b></div>
    <div class="bar"><span>Marketing</span><div class="track"><div class="fill" data-w="15"></div></div><b>15%</b></div>
    <div class="bar"><span>Promo</span><div class="track"><div class="fill" data-w="10"></div></div><b>10%</b></div>
  </div>
  <p class="small muted" style="margin-top:12px"><b>Ops</b>: hosting, tools, research. <b>Talent</b>: hiring writers, editors, translators and creators. <b>Prizes</b>: contests and giveaways. <b>Marketing / Promo</b>: growing the community and festival promotions. Target split; updated in periodic reports.</p>
</div></section>
<section id="pledge"><div class="wrap grid g2">
  <div><h2>Pledge, sponsor or give in kind</h2><p class="muted">Prefer bank transfer, UPI, crypto or an invoice for company sponsorship? Or want to donate prizes, services or hosting? Send a pledge and we'll reply with details.</p>
  <p class="small muted">09911.com is not a registered charity. Contributions are not tax-deductible, and they don't buy editorial influence.</p></div>
  <form class="form-card" data-form="Donation Pledge" data-ok="Thank you for your support! ♥ We'll email payment details shortly.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="g-n">Name</label><input id="g-n" name="name" required></div><div><label for="g-e">Email</label><input id="g-e" type="email" name="email" required></div></div>
    <div class="row"><div><label for="g-a">Amount (USD)</label><input id="g-a" type="number" name="amount" min="1" value="19"></div><div><label for="g-f">Frequency</label><select id="g-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
    <label for="g-u">Allocate to</label><select id="g-u" name="allocate"><option>Where most needed</option><option>Operations</option><option>Contests &amp; prizes</option><option>Hiring talent</option><option>Marketing &amp; promotions</option></select>
    <label for="g-m">Method / message</label><textarea id="g-m" name="message" placeholder="e.g. PayPal, bank transfer, UPI, prize donation…"></textarea>
    <label class="check" style="margin-top:10px"><input type="checkbox" name="public" value="yes"> List my name on the supporters wall</label>
    <button class="btn btn-gold btn-block" style="margin-top:12px" type="submit">Send pledge ♥</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
"""
    return ("donate.html", "Support 09911 — Donate to Keep Festival Guides Free",
            "Donate to fund operations, contests and prizes, hiring writers and creators, and promotions for the independent 09911 festival guide.", body)


def careers():
    roles = [("Deal Editor (remote, part-time)", "Verify and publish festival deals; SEA time zones preferred."),
             ("Chinese–English Culture Writer", "Write number-culture and festival explainers. Mandarin required."),
             ("Video Creator / Editor", "Short-form hauls, stacking tutorials and festival explainers."),
             ("Community Manager — SEA", "Run Telegram/WhatsApp alert channels and contests."),
             ("SEO &amp; Growth Marketer", "Grow organic and social traffic ahead of each festival."),
             ("Front-end Developer (freelance)", "Static-site features: calculators, trackers, i18n.")]
    cards = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p><a class="btn btn-sm btn-ghost" href="#apply" onclick="document.getElementById(\'j-r\').value=this.parentNode.querySelector(\'h3\').textContent">Apply</a></div>' for t, d in roles)
    body = page_hero("Careers, freelancers &amp; creators", "Help build the go-to guide for the global festival season. Remote-first, paid per project or part-time.", "Careers") + f"""
<section style="padding-top:10px"><div class="wrap grid g3">{cards}</div></section>
<section class="section-alt" id="apply"><div class="wrap grid g2">
  <div id="creators"><h2>Apply or pitch</h2><p class="muted">Send a short note and your portfolio link. Creators can also pitch paid festival collaborations.</p></div>
  <form class="form-card" data-form="Job / Creator Application" data-ok="Application received! We'll reply if there's a fit.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="j-n">Name</label><input id="j-n" name="name" required></div><div><label for="j-e">Email</label><input id="j-e" type="email" name="email" required></div></div>
    <label for="j-r">Role</label><input id="j-r" name="role" required placeholder="e.g. Deal Editor">
    <div class="row"><div><label for="j-p">Portfolio / LinkedIn / channel</label><input id="j-p" type="url" name="portfolio" placeholder="https://"></div><div><label for="j-t">Time zone</label><input id="j-t" name="timezone"></div></div>
    <label for="j-m">Why you?</label><textarea id="j-m" name="message" required></textarea>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Send application</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
"""
    return ("careers.html", "Careers & Creator Program | 09911",
            "Remote roles for deal editors, Chinese-English writers, video creators, community managers and developers at 09911.", body)


def about():
    body = page_hero("About 09911", "One domain, two readings: a season and a sentiment.", "About") + f"""
<section style="padding-top:10px"><div class="wrap prose">
  <h2>The name</h2>
  <p><b>As a calendar:</b> 0 → 9.9 → 11.11, from the start of the season through the two biggest double-date festivals.</p>
  <p><b>As sound:</b> <i>líng jiǔ jiǔ yāo yāo</i>. 九九 (99) echoes 久久, "forever". 11 is "Double Eleven", Singles' Day.</p>
  <h2>What we do</h2>
  <ul><li>Track every double-date and Chinese festival with countdowns and calendar reminders</li><li>Publish platform guides and stacking strategies</li><li>Explain the culture behind the numbers</li><li>Run fair, free contests and support creators</li></ul>
  <h2>Editorial independence</h2>
  <p>Guides are written for shoppers, not sponsors. Sponsored placements are always labelled, and rankings are never sold. Read our <a href="legal.html#affiliate">affiliate disclosure</a>.</p>
  <p><a class="btn btn-primary" href="contact.html">Get in touch</a> <a class="btn btn-ghost" href="{CONTACT}" target="_blank" rel="noopener">Domain / partnership enquiries ↗</a></p>
</div></section>
{lead_box()}
"""
    return ("about.html", "About 09911 — The Festival Season Hub", "What 09911 means, what we publish and how we stay independent.", body)


def contact():
    body = page_hero("Contact us", "Questions, corrections, press, partnerships: we read everything.", "Contact") + f"""
<section style="padding-top:10px"><div class="wrap grid g2">
  <div>
    <div class="card"><h3>Domain, sponsorship, advertising or partnership?</h3><p>For acquisition of 09911.com, sponsorship, advertising and partnerships, use the owner's contact page:</p><a class="btn btn-gold" href="{CONTACT}" target="_blank" rel="noopener">web.works/contact ↗</a></div>
    <div class="card" style="margin-top:16px"><h3>Everything else</h3><p>Use the form. Messages go straight to the team; your data is used only to reply (see <a href="legal.html#privacy">privacy</a>).</p></div>
  </div>
  <form class="form-card" data-form="Contact" data-ok="Message sent! We'll get back to you soon.">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <div class="row"><div><label for="ct-n">Name</label><input id="ct-n" name="name" required autocomplete="name"></div><div><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required autocomplete="email"></div></div>
    <label for="ct-t">Topic</label><select id="ct-t" name="topic"><option>General question</option><option>Advertising</option><option>Sponsorship</option><option>Partnership</option><option>Domain name enquiry</option><option>Press</option><option>Correction</option><option>Copyright / takedown</option></select>
    <label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea>
    <button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Send message</button><div class="form-msg" role="status"></div>
  </form>
</div></section>
"""
    return ("contact.html", "Contact 09911", "Contact the 09911 team about advertising, sponsorship, partnerships, the domain name, press or corrections.", body)


def legal():
    body = page_hero("Legal, trademark &amp; disclosures", "Plain-English policies. Last updated September 2026.", "Legal") + f"""
<section style="padding-top:10px"><div class="wrap prose">
  <h2 id="disclosure">Trademark &amp; copyright disclosure</h2>
  <ul>
    <li><b>The name.</b> "09911" is the domain name 09911.com and a numeric identifier. It is used as a descriptive reference to the festival season (9.9 to 11.11) and to Chinese number culture. We claim no exclusive rights in the numbers 0, 9, 99, 11, 911 or any combination of them, and no rights in any third party's number-based marks.</li>
    <li><b>Not "911".</b> 09911 has no connection with any emergency service, the "911" emergency number or any event associated with 11 September. It must not be used to reach emergency services.</li>
    <li><b>Third-party marks.</b> Alibaba, Taobao, Tmall, Juhuasuan, AliExpress, Lazada, Shopee, JD.com, Amazon, Prime, TikTok, Temu, YouTube, Google and AdSense are trademarks of their respective owners. Festival names such as "Double 11", "双11", "Singles' Day", "99划算节", "618" and "12.12" may be registered trademarks of their owners in some jurisdictions. They are used here only nominatively, to identify the events we write about. 09911 is <b>not affiliated with, sponsored by or endorsed by</b> any of these companies.</li>
    <li><b>Our copyright.</b> Text, layout, graphics, calculators and source code on this site are © 09911.com, all rights reserved, unless stated otherwise. Short quotations with a link back are welcome.</li>
    <li><b>Third-party content.</b> Statistics are attributed to their sources. Embedded videos remain the property of their creators and are shown via YouTube's embed player under YouTube's terms. Chinese characters, festival customs and number meanings are part of the public cultural heritage.</li>
    <li><b>Takedown.</b> If you believe content here infringes your rights, send details through the <a href="contact.html">contact form</a> (topic: Copyright / takedown). We respond promptly.</li>
  </ul>
  <h2 id="affiliate">Affiliate &amp; advertising disclosure</h2>
  <p>Some outbound links are affiliate links. If you buy through them we may earn a commission, at no extra cost to you. We show ads (including Google AdSense) and sell clearly labelled sponsored placements. Neither affects our editorial guides or rankings.</p>
  <h2 id="privacy">Privacy policy</h2>
  <ul>
    <li><b>Forms:</b> the data you submit (e.g. name, email, message) is sent through the FormSubmit service to our private inbox and used only to respond, send the alerts you asked for, or run contests. We never sell personal data.</li>
    <li><b>Cookies &amp; ads:</b> Google and its partners may use cookies to serve ads based on your visits to this and other sites. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. If analytics is enabled, Google Analytics collects anonymous usage data.</li>
    <li><b>Local storage:</b> we store your theme choice and whether you've dismissed pop-ups, in your browser only.</li>
    <li><b>Your rights:</b> ask for access, correction or deletion at any time via the <a href="contact.html">contact form</a>. Every email includes an unsubscribe link.</li>
  </ul>
  <h2 id="terms">Terms of use</h2>
  <ul>
    <li>Content is for general information and entertainment. Prices, vouchers and dates change; always confirm on the official platform before buying.</li>
    <li>Number-meaning tools are cultural entertainment, not financial, legal or life advice.</li>
    <li>Contests: no purchase necessary, open to adults (18+) where lawful, void where prohibited, winners drawn at random. We may cancel or change a contest if required by law or in cases of fraud.</li>
    <li>Donations are voluntary, non-refundable except where required by law, and not tax-deductible.</li>
    <li>The site is provided "as is", without warranties. To the extent permitted by law, we are not liable for losses arising from use of the site or third-party platforms.</li>
  </ul>
</div></section>
"""
    return ("legal.html", "Legal, Trademark & Copyright Disclosure, Privacy, Terms | 09911",
            "09911.com trademark and copyright disclosure, affiliate disclosure, privacy policy and terms of use.", body)


def notfound():
    body = page_hero("404: this page took a holiday", "Probably shopping. Try the calendar or the homepage.", "404") + """
<section><div class="wrap"><a class="btn btn-primary" href="index.html">Go home</a> <a class="btn btn-ghost" href="calendar.html">Festival calendar</a></div></section>"""
    return ("404.html", "Page not found | 09911", "Page not found.", body)


PAGES_B = [stats(), videos(), contests(), advertise(), donate(), careers(), about(), contact(), legal(), notfound()]
