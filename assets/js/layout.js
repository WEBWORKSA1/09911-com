/* 09911.com — shared layout: header, footer, alert modal and lead boxes (one place to edit). */
(function () {
  "use strict";
  var CONTACT = "https://web.works/contact";
  var NAV = [["index.html", "Home"], ["calendar.html", "Calendar"], ["9-9.html", "9.9"], ["11-11.html", "11.11"], ["festivals.html", "Festivals"], ["deals.html", "Deals"],
    ["numbers.html", "Lucky Numbers"], ["stats.html", "Stats"], ["videos.html", "Videos"], ["contests.html", "Contests"]];
  var brand = function (dark) {
    return '<span class="logo">099<br>11</span><span>09911<small' + (dark ? ' style="color:#c9ad98"' : "") + ">9.9 → 11.11 · FESTIVAL SEASON HUB</small></span>";
  };

  var h = document.getElementById("site-header");
  if (h) {
    var page = h.getAttribute("data-page") || "";
    h.outerHTML = '<header class="site-header"><div class="wrap nav">' +
      '<a class="brand" href="index.html" aria-label="09911 home">' + brand() + "</a>" +
      '<nav class="menu" id="menu" aria-label="Main">' + NAV.map(function (n) { return '<a href="' + n[0] + '"' + (n[0] === page ? ' aria-current="page"' : "") + ">" + n[1] + "</a>"; }).join("") +
      '<a class="btn btn-primary btn-sm" href="advertise.html" style="color:#fff">Advertise</a></nav>' +
      '<div class="nav-tools"><button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">◐</button>' +
      '<button class="icon-btn burger" aria-controls="menu" aria-expanded="false" aria-label="Open menu">☰</button></div></div></header>';
  }

  var OPTS = ["Global", "Singapore", "Malaysia", "Philippines", "Indonesia", "Thailand", "Vietnam", "China", "India", "USA", "Canada", "UK", "Australia", "Other"];
  var PLAT = ["Shopee", "Lazada", "AliExpress", "Taobao/Tmall", "Amazon", "TikTok Shop", "Temu"];
  Array.prototype.forEach.call(document.querySelectorAll("[data-leadbox]"), function (el) {
    var src = el.getAttribute("data-leadbox") || "alerts";
    var title = el.getAttribute("data-title") || "Never miss a mega sale again";
    var sub = el.getAttribute("data-sub") || "Free alerts before every double-date festival — 9.9, 10.10, 11.11, 12.12, 618 &amp; Chinese New Year — plus stacking guides and exclusive codes.";
    el.outerHTML = '<section id="alerts"><div class="wrap"><div class="lead-box reveal"><div>' +
      '<span class="eyebrow" style="background:rgba(255,255,255,.18);color:#fff">Free · 1-click unsubscribe</span>' +
      '<h2 style="margin-top:12px">' + title + "</h2><p>" + sub + "</p>" +
      '<ul><li>24-hour and 1-hour "goes live" reminders</li><li>Only the platforms and countries you pick</li><li>Voucher-stacking cheat-sheets &amp; monthly giveaway entries</li></ul>' +
      '<span class="social-proof">🔒 No spam. We never sell your data.</span></div>' +
      '<form data-form="Deal Alerts (' + src + ')" data-ok="You\'re in! Watch your inbox before the next festival goes live. 🎉" novalidate>' +
      '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">' +
      '<label for="la-email-' + src + '">Email</label><input id="la-email-' + src + '" type="email" name="email" required placeholder="you@example.com" autocomplete="email">' +
      '<div class="row"><div><label for="la-country-' + src + '">Country</label><select id="la-country-' + src + '" name="country">' + OPTS.map(function (o) { return "<option>" + o + "</option>"; }).join("") + "</select></div>" +
      '<div><label for="la-when-' + src + '">Alert me for</label><select id="la-when-' + src + '" name="festivals"><option>All festivals</option><option>11.11 only</option><option>9.9 &amp; 11.11</option><option>12.12 &amp; year-end</option><option>618 mid-year</option><option>Chinese festivals</option></select></div></div>' +
      '<label>Platforms I shop</label><div class="seg">' + PLAT.map(function (p) { return '<label><input type="checkbox" name="platforms" value="' + p + '"><span>' + p + "</span></label>"; }).join("") + "</div>" +
      '<label class="check" style="margin-top:12px"><input type="checkbox" name="consent" value="yes" required> I agree to receive festival alerts and accept the <a href="legal.html#privacy">privacy policy</a>.</label>' +
      '<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Get free alerts →</button><div class="form-msg" role="status"></div></form></div></div></section>';
  });

  var f = document.getElementById("site-footer");
  if (f) {
    var li = function (a) { return a.map(function (x) { return '<li><a href="' + x[0] + '"' + (/^https/.test(x[0]) ? ' target="_blank" rel="noopener"' : "") + ">" + x[1] + "</a></li>"; }).join(""); };
    f.outerHTML = '<footer class="site-footer"><div class="wrap"><div class="foot-grid"><div>' +
      '<a class="brand" href="index.html" style="color:#fff">' + brand(true) + "</a>" +
      '<p class="small" style="margin-top:12px">An independent guide to the world\'s double-date shopping festivals and the Chinese number culture behind them. We are not affiliated with any retailer or platform mentioned.</p>' +
      '<p><a class="btn btn-gold btn-sm" href="donate.html">♥ Support 09911</a></p></div>' +
      "<div><h4>Explore</h4><ul>" + li([["calendar.html", "Festival calendar"], ["9-9.html", "9.9 &amp; 99 Mega Sale"], ["11-11.html", "11.11 Singles' Day"], ["festivals.html", "All festivals"], ["deals.html", "Platforms &amp; stacking"], ["numbers.html", "Lucky numbers"], ["stats.html", "GMV statistics"], ["videos.html", "Videos"]]) + "</ul></div>" +
      "<div><h4>Get involved</h4><ul>" + li([["advertise.html", "Advertise / get featured"], ["advertise.html#partner", "Sponsorship &amp; partnership"], ["deals.html#submit", "Submit a deal"], ["contests.html", "Contests &amp; prizes"], ["careers.html", "Careers &amp; creators"], ["donate.html", "Donate"], [CONTACT, "Buy / partner on this domain"]]) + "</ul></div>" +
      "<div><h4>Company</h4><ul>" + li([["about.html", "About"], ["contact.html", "Contact"], ["legal.html#disclosure", "Trademark &amp; copyright"], ["legal.html#affiliate", "Affiliate disclosure"], ["legal.html#privacy", "Privacy"], ["legal.html#terms", "Terms"], ["sitemap.xml", "Sitemap"]]) + "</ul></div></div>" +
      '<div class="legal-note">© <span data-year>2026</span> 09911.com. Original content, design and code © 09911.com; all rights reserved. "09911" is used here as a domain name and descriptive numeric identifier; no claim is made over the numbers 0, 9, 99, 11 or 911. All third-party names (e.g. Alibaba, Taobao, Tmall, Shopee, Lazada, AliExpress, JD.com, Amazon, TikTok, Temu, YouTube, Google) and festival names such as "Double 11"/"双11" are trademarks of their respective owners, used for identification only, with no endorsement implied. Some links are affiliate links; we may earn a commission at no cost to you. <a href="legal.html#disclosure">Full disclosure</a>.</div></div></footer>' +
      '<div class="modal" id="alert-modal" role="dialog" aria-modal="true" aria-labelledby="m-t"><div class="box">' +
      '<button class="icon-btn close" data-close aria-label="Close">✕</button><span class="badge b-hot">Before you go</span>' +
      '<h3 id="m-t" style="margin-top:10px">Get the next mega sale in your inbox</h3><p class="muted small">One reminder 24h before, one when it goes live. That\'s it.</p>' +
      '<form data-form="Deal Alerts (exit modal)" data-ok="Done! We\'ll ping you before the next festival."><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">' +
      '<label for="m-email">Email</label><input id="m-email" type="email" name="email" required placeholder="you@example.com">' +
      '<label class="check" style="margin-top:10px"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="legal.html#privacy">privacy policy</a>.</label>' +
      '<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Remind me</button><div class="form-msg" role="status"></div></form></div></div>' +
      '<div class="toast" role="status" aria-live="polite"></div>' +
      '<div class="sticky-cta"><a class="btn btn-primary btn-sm" href="#alerts" data-open-modal>🔔 Alerts</a></div>';
  }
})();
