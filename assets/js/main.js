/* 09911.com — main script. Vanilla JS, no dependencies. */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Theme ---------- */
  var saved = store("theme"); if (saved) document.documentElement.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") ||
        (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var next = cur === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next); store("theme", next);
    });
  });

  /* ---------- Mobile menu ---------- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () {
    var o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", o);
  });

  /* ---------- Year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Event engine (all times = 00:00 UTC+8, when Asian platforms go live) ---------- */
  var LUNAR = {
    2026: { cny: [2, 17], qixi: [8, 19], midautumn: [9, 25], chongyang: [10, 18], dragon: [6, 19] },
    2027: { cny: [2, 6], qixi: [8, 8], midautumn: [9, 15], chongyang: [10, 8], dragon: [6, 9] },
    2028: { cny: [1, 26], qixi: [8, 26], midautumn: [10, 3], chongyang: [10, 26], dragon: [5, 28] }
  };
  function at(y, m, d) { return new Date(Date.UTC(y, m - 1, d, -8, 0, 0)); }
  function nthWeekday(y, m, wd, n) { var d = new Date(Date.UTC(y, m - 1, 1)); var off = (wd - d.getUTCDay() + 7) % 7; return 1 + off + (n - 1) * 7; }
  function buildEvents(y0, y1) {
    var ev = [];
    for (var y = y0; y <= y1; y++) {
      [3, 4, 5, 6, 7, 8, 10].forEach(function (m) {
        ev.push({ id: m + "-" + m, t: m + "." + m + " Sale", d: at(y, m, m), type: "sale", url: "calendar.html", note: "Monthly double-date mega sale on Shopee, Lazada, TikTok Shop & more." });
      });
      ev.push({ id: "9-9", t: "9.9 Super Shopping Day + Taobao 99 Mega Sale", d: at(y, 9, 9), type: "mega", url: "9-9.html", note: "The season opener: 9.9 across Southeast Asia and the 99 sale in China." });
      ev.push({ id: "11-11", t: "11.11 Singles' Day", d: at(y, 11, 11), type: "mega", url: "11-11.html", note: "The world's largest shopping festival by GMV." });
      ev.push({ id: "12-12", t: "12.12 Year-End Sale", d: at(y, 12, 12), type: "mega", url: "festivals.html#s1212", note: "Last double date of the year — clearance, gifts, year-end vouchers." });
      ev.push({ id: "618", t: "618 Mid-Year Festival", d: at(y, 6, 18), type: "mega", url: "festivals.html#s618", note: "China's mid-year festival, anchored by JD.com's anniversary." });
      ev.push({ id: "520", t: "520 Online Valentine's (我爱你)", d: at(y, 5, 20), type: "culture", url: "numbers.html#n520", note: "5-2-0 sounds like 'I love you' — gifting and flowers peak." });
      var bf = nthWeekday(y, 11, 5, 4);
      ev.push({ id: "bf", t: "Black Friday", d: new Date(Date.UTC(y, 10, bf, 5)), type: "sale", url: "festivals.html#sbf", note: "Western mega-sale; global platforms run parallel campaigns." });
      ev.push({ id: "cm", t: "Cyber Monday", d: new Date(Date.UTC(y, 10, bf + 3, 5)), type: "sale", url: "festivals.html#sbf", note: "Online-only follow-up to Black Friday." });
      var L = LUNAR[y];
      if (L) {
        ev.push({ id: "cny", t: "Chinese New Year", d: at(y, L.cny[0], L.cny[1]), type: "culture", url: "festivals.html#scny", note: "Spring Festival. Pre-CNY sales run 2–3 weeks earlier." });
        ev.push({ id: "qixi", t: "Qixi (Chinese Valentine's)", d: at(y, L.qixi[0], L.qixi[1]), type: "culture", url: "festivals.html#sqixi", note: "7th day of the 7th lunar month." });
        ev.push({ id: "midautumn", t: "Mid-Autumn Festival", d: at(y, L.midautumn[0], L.midautumn[1]), type: "culture", url: "festivals.html#smid", note: "Mooncake season." });
        ev.push({ id: "chongyang", t: "Double Ninth (Chongyang) 重阳节", d: at(y, L.chongyang[0], L.chongyang[1]), type: "culture", url: "9-9.html#chongyang", note: "9th day of 9th lunar month — honouring elders, longevity (久久)." });
        ev.push({ id: "dragon", t: "Dragon Boat Festival", d: at(y, L.dragon[0], L.dragon[1]), type: "culture", url: "festivals.html#scny", note: "5th day of 5th lunar month." });
      }
    }
    return ev.sort(function (a, b) { return a.d - b.d; });
  }
  var NOW = new Date(); var Y = NOW.getFullYear();
  var EVENTS = buildEvents(Y - 0, Y + 1);
  window.EVENTS_09911 = EVENTS;
  var DAY = 864e5;
  function upcoming(filter) { return EVENTS.filter(function (e) { return e.d.getTime() + DAY > Date.now() && (!filter || filter(e)); }); }

  /* ---------- Countdown ---------- */
  var cd = $("[data-countdown]");
  if (cd) {
    var chipsBox = $("[data-cd-chips]", cd.parentNode) || $("[data-cd-chips]");
    var list = upcoming(function (e) { return e.type !== "culture" || e.id === "chongyang" || e.id === "cny"; }).slice(0, 8);
    var pref = cd.getAttribute("data-countdown");
    var cur = list.filter(function (e) { return e.id === pref; })[0] || list[0];
    if (chipsBox) {
      chipsBox.innerHTML = list.map(function (e, i) {
        return '<button class="chip' + (e === cur ? " active" : "") + '" data-i="' + i + '">' + e.t.split(" ")[0] + " · " + fmtShort(e.d) + "</button>";
      }).join("");
      chipsBox.addEventListener("click", function (ev) {
        var b = ev.target.closest(".chip"); if (!b) return;
        $$(".chip", chipsBox).forEach(function (c) { c.classList.remove("active"); });
        b.classList.add("active"); cur = list[+b.getAttribute("data-i")]; tick();
      });
    }
    function tick() {
      if (!cur) return;
      var diff = cur.d - Date.now();
      $("[data-cd-title]").innerHTML = '<a href="' + cur.url + '" style="color:#fff">' + cur.t + "</a>";
      $("[data-cd-note]").textContent = cur.note + " Starts " + cur.d.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }) + " (your time).";
      if (diff <= 0 && diff > -DAY) {
        $("[data-cd-label]").innerHTML = '<span class="cd-live">LIVE NOW</span> ends in';
        diff = cur.d.getTime() + DAY - Date.now();
      } else { $("[data-cd-label]").textContent = "Next festival starts in"; }
      var s = Math.max(0, Math.floor(diff / 1000));
      var parts = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      $$("b", cd).forEach(function (b, i) { b.textContent = String(parts[i]).padStart(2, "0"); });
    }
    tick(); setInterval(tick, 1000);
  }
  function fmtShort(d) { return d.toLocaleDateString(undefined, { month: "short", day: "numeric", timeZone: "Asia/Singapore" }); }

  /* ---------- Calendar page ---------- */
  var tl = $("[data-timeline]");
  if (tl) {
    var type = "all";
    function renderTl() {
      var items = EVENTS.filter(function (e) { return type === "all" || e.type === type; });
      tl.innerHTML = items.map(function (e) {
        var past = e.d.getTime() + DAY < Date.now();
        var days = Math.ceil((e.d - Date.now()) / DAY);
        var tag = past ? '<span class="badge b-soon">Past</span>' : days <= 0 ? '<span class="badge b-live">Live</span>' : days <= 14 ? '<span class="badge b-hot">In ' + days + "d</span>" : '<span class="badge b-gold">In ' + days + "d</span>";
        return '<li class="' + (past ? "past" : "") + '"><div class="date">' + e.d.toLocaleDateString(undefined, { day: "numeric", month: "short", year: "numeric", timeZone: "Asia/Singapore" }) + "</div><div><b><a href=\"" + e.url + "\">" + e.t + "</a></b><div class=\"small muted\">" + e.note + "</div></div><div>" + tag + ' <button class="btn btn-sm btn-ghost" data-ics="' + EVENTS.indexOf(e) + '">+ Calendar</button></div></li>';
      }).join("");
    }
    renderTl();
    $$("[data-tl-filter]").forEach(function (b) {
      b.addEventListener("click", function () {
        $$("[data-tl-filter]").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active"); type = b.getAttribute("data-tl-filter"); renderTl();
      });
    });
  }
  function icsFor(list) {
    function f(d) { return d.toISOString().replace(/[-:]/g, "").split(".")[0] + "Z"; }
    var out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//09911.com//Festival Calendar//EN", "CALSCALE:GREGORIAN"];
    list.forEach(function (e, i) {
      out.push("BEGIN:VEVENT", "UID:" + e.id + "-" + e.d.getTime() + "-" + i + "@09911.com", "DTSTAMP:" + f(new Date()), "DTSTART:" + f(e.d), "DTEND:" + f(new Date(e.d.getTime() + DAY)),
        "SUMMARY:" + e.t, "DESCRIPTION:" + e.note + " More: https://09911.com/" + e.url, "BEGIN:VALARM", "TRIGGER:-PT12H", "ACTION:DISPLAY", "DESCRIPTION:" + e.t + " starts soon", "END:VALARM", "END:VEVENT");
    });
    out.push("END:VCALENDAR");
    var blob = new Blob([out.join("\r\n")], { type: "text/calendar" });
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = (list.length === 1 ? list[0].id : "09911-festival-calendar") + ".ics";
    document.body.appendChild(a); a.click(); a.remove();
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest("[data-ics]"); if (!b) return;
    var v = b.getAttribute("data-ics");
    icsFor(v === "all" ? upcoming() : [EVENTS[+v]]);
  });

  /* ---------- Forms (FormSubmit AJAX; address assembled at runtime, never rendered) ---------- */
  function endpoint() {
    if (C.FORM_ALIAS) return "https://formsubmit.co/ajax/" + C.FORM_ALIAS;
    return "https://formsubmit.co/ajax/" + (C._k || []).map(function (n) { return String.fromCharCode(n - 7); }).reverse().join("");
  }
  $$("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var msg = $(".form-msg", form) || form.appendChild(Object.assign(document.createElement("div"), { className: "form-msg" }));
      var hp = form.querySelector("[name=_honey]"); if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = {}; new FormData(form).forEach(function (v, k) { if (k !== "_honey") data[k] = data[k] ? data[k] + ", " + v : v; });
      data._subject = "[09911.com] " + form.getAttribute("data-form") + " — " + (data.name || data.email || "new submission");
      data._template = "table"; data.form = form.getAttribute("data-form"); data.page = location.pathname; data.submitted = new Date().toISOString();
      var btn = form.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false") throw new Error(j.message || "fail"); }); })
        .then(function () {
          msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-ok") || "Thank you! We received your submission and will be in touch.";
          form.reset(); store("lead", "1"); if (window.gtag) gtag("event", "generate_lead", { form: data.form });
        })
        .catch(function () {
          msg.className = "form-msg err"; msg.innerHTML = 'Something went wrong. Please try again, or reach us via <a href="' + (C.CONTACT_URL || "#") + '" target="_blank" rel="noopener">our contact page</a>.';
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  });

  /* ---------- Chinese number meanings + checker ---------- */
  var DIG = {
    "0": { h: "零", p: "líng", m: "Wholeness, a fresh start; slang for 你 (you)", s: 1 },
    "1": { h: "一", p: "yī / yāo", m: "Unity, the one; 'yāo' echoes 要 (want)", s: 1 },
    "2": { h: "二", p: "èr", m: "Pairs & harmony — 'good things come in pairs'", s: 2 },
    "3": { h: "三", p: "sān", m: "Sounds like 生 (life/birth)", s: 1 },
    "4": { h: "四", p: "sì", m: "Sounds like 死 (death) — the most avoided digit", s: -3 },
    "5": { h: "五", p: "wǔ", m: "Five elements; slang for 我 (I)", s: 0 },
    "6": { h: "六", p: "liù", m: "Sounds like 流 (flow) — smooth progress", s: 2 },
    "7": { h: "七", p: "qī", m: "Togetherness (起); mixed — 7th lunar month is Ghost Month", s: 0 },
    "8": { h: "八", p: "bā", m: "Sounds like 发 (prosper) — the luckiest digit", s: 3 },
    "9": { h: "九", p: "jiǔ", m: "Sounds like 久 (long-lasting) — longevity, eternity", s: 3 }
  };
  var COMBO = [
    ["1314", "一生一世 — 'one life, one world' (forever)", 4], ["520", "我爱你 — 'I love you'", 3], ["521", "我愿意 — 'I'm willing'", 2],
    ["168", "一路发 — 'prosper all the way'", 4], ["518", "我要发 — 'I will prosper'", 3], ["888", "发发发 — triple prosperity", 5],
    ["666", "溜溜溜 — 'smooth / awesome'", 3], ["99", "久久 — forever, eternal", 3], ["88", "双发 — double prosperity (also 'bye-bye')", 2],
    ["11", "Double eleven — Singles' Day, 'one and one'", 1], ["14", "要死 — sounds like 'want to die'", -3], ["24", "Sounds like 'easy to die'", -2],
    ["250", "二百五 — slang for 'fool'", -2], ["514", "我要死 — 'I want to die'", -3], ["748", "去死吧 — 'go die'", -3], ["4", "", 0]
  ];
  window.NUM09911 = { DIG: DIG, COMBO: COMBO };
  var chk = $("[data-checker]");
  if (chk) {
    var input = $("#num-input"), out = $("#num-out");
    function analyse(v) {
      var d = (v || "").replace(/\D/g, "").slice(0, 24);
      if (!d) { out.innerHTML = '<p class="muted">Type any number — a phone number, licence plate, birthday (e.g. 19990911), price or domain.</p>'; return; }
      var score = 0, cells = "", found = [];
      d.split("").forEach(function (c) { var x = DIG[c]; score += x.s; cells += '<div class="digit ' + (x.s > 1 ? "good" : x.s < 0 ? "bad" : "") + '" title="' + x.m + '"><b>' + c + '</b><small>' + x.h + "</small></div>"; });
      COMBO.forEach(function (k) { if (k[1] && d.indexOf(k[0]) > -1) { score += k[2]; found.push("<li><b>" + k[0] + "</b> — " + k[1] + "</li>"); } });
      var cnt = {}; d.split("").forEach(function (c) { cnt[c] = (cnt[c] || 0) + 1; });
      var pct = Math.max(3, Math.min(100, Math.round(50 + score * 30 / Math.sqrt(d.length))));
      var verdict = pct >= 80 ? "Very auspicious ✨" : pct >= 60 ? "Auspicious 👍" : pct >= 40 ? "Neutral" : "Traditionally avoided";
      var top = Object.keys(cnt).sort(function (a, b) { return cnt[b] - cnt[a]; })[0];
      out.innerHTML = '<div class="digits">' + cells + "</div>" +
        '<div class="meter" aria-label="Luck score"><i style="width:' + pct + '%"></i></div>' +
        '<p style="margin-top:10px"><b style="font-size:1.4rem">' + pct + "/100</b> · " + verdict + "</p>" +
        "<p class=\"small\">Dominant digit <b>" + top + " (" + DIG[top].h + ", " + DIG[top].p + ")</b>: " + DIG[top].m + ".</p>" +
        (found.length ? "<h4>Hidden phrases</h4><ul>" + found.join("") + "</ul>" : "<p class=\"small muted\">No classic phrases found.</p>") +
        '<p class="small muted">For entertainment and cultural education. Based on common Mandarin homophones.</p>';
    }
    input.addEventListener("input", function () { analyse(input.value); });
    $$("[data-try]").forEach(function (b) { b.addEventListener("click", function () { input.value = b.getAttribute("data-try"); analyse(input.value); input.focus(); }); });
    analyse(input.value);
  }

  /* ---------- Animated bars ---------- */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (en) {
    en.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      $$(".fill", e.target).forEach(function (f) { f.style.width = f.getAttribute("data-w") + "%"; });
      io.unobserve(e.target);
    });
  }, { threshold: .15 }) : null;
  $$(".reveal,.bars").forEach(function (el) { if (io) io.observe(el); else { el.classList.add("in"); $$(".fill", el).forEach(function (f) { f.style.width = f.getAttribute("data-w") + "%"; }); } });

  setTimeout(function () { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); $$(".fill").forEach(function (f) { f.style.width = f.getAttribute("data-w") + "%"; }); }, 2500);

  /* ---------- YouTube (privacy-friendly click-to-load) ---------- */
  var vids = $("[data-videos]");
  if (vids) {
    var ids = C.YOUTUBE_VIDEOS || [];
    var topics = [["11.11 haul & unboxing", "11.11 sale haul"], ["How to stack vouchers", "shopee lazada voucher stacking guide"], ["Singles' Day explained", "singles day explained documentary"],
      ["9.9 sale tips", "9.9 sale tips"], ["Chinese lucky numbers", "chinese lucky numbers meaning"], ["Double Ninth Festival", "double ninth festival chongyang"]];
    if (ids.length) {
      vids.innerHTML = ids.map(function (id) { return '<div class="video" data-yt="' + id + '"><div class="ph"><div><div class="play">▶</div>Click to play</div></div></div>'; }).join("");
    } else {
      vids.innerHTML = topics.map(function (t) {
        return '<a class="video" href="https://www.youtube.com/results?search_query=' + encodeURIComponent(t[1]) + '" target="_blank" rel="noopener"><div class="ph"><div><div class="play">▶</div><b>' + t[0] + '</b><div class="small">Watch on YouTube</div></div></div></a>';
      }).join("");
    }
    vids.addEventListener("click", function (e) {
      var v = e.target.closest("[data-yt]"); if (!v || v.querySelector("iframe")) return;
      v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute("data-yt") + '?autoplay=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Video"></iframe>';
    });
  }

  /* ---------- AdSense (activates only when configured) ---------- */
  if (C.ADSENSE_CLIENT) {
    var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.ADSENSE_CLIENT;
    document.head.appendChild(s);
    $$(".ad-slot").forEach(function (slot) {
      var key = slot.getAttribute("data-ad") || "inContent";
      slot.setAttribute("data-live", "1");
      slot.innerHTML = '<ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + C.ADSENSE_CLIENT + '"' + (C.ADSENSE_SLOTS && C.ADSENSE_SLOTS[key] ? ' data-ad-slot="' + C.ADSENSE_SLOTS[key] + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
  }
  /* ---------- GA4 ---------- */
  if (C.GA4_ID) {
    var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.GA4_ID; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", C.GA4_ID);
  }

  /* ---------- Donate buttons ---------- */
  $$("[data-donate]").forEach(function (a) {
    var k = a.getAttribute("data-donate"), url = C.DONATE && C.DONATE[k];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; } else { a.href = "donate.html#pledge"; }
  });
  /* ---------- Affiliate links ---------- */
  $$("[data-aff]").forEach(function (a) { var u = C.AFFILIATE && C.AFFILIATE[a.getAttribute("data-aff")]; if (u) a.href = u; });

  /* ---------- Exit-intent / timed alert modal ---------- */
  var modal = $("#alert-modal");
  if (modal && !store("lead") && !store("modal-seen")) {
    var shown = false;
    function show() { if (shown) return; shown = true; modal.classList.add("open"); store("modal-seen", String(Date.now())); }
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 10) show(); });
    setTimeout(show, 45000);
  }
  $$("[data-close]").forEach(function (b) { b.addEventListener("click", function () { b.closest(".modal").classList.remove("open"); }); });
  $$("[data-open-modal]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); modal && modal.classList.add("open"); }); });

  /* ---------- Social-proof toast (rotates real site facts, not fabricated activity) ---------- */
  var toast = $(".toast");
  if (toast) {
    var facts = ["💡 Tip: 11.11 deals go live at 00:00 UTC+8 — add it to your calendar.", "🧧 9 (九, jiǔ) sounds like 久 — 'long-lasting'.", "📅 Download the full double-date calendar (.ics) — free.", "🎁 Monthly giveaway open — one entry per person.", "📣 Brands: get featured before the next mega sale."];
    var fi = 0;
    setTimeout(function loop() { toast.textContent = facts[fi++ % facts.length]; toast.classList.add("show"); setTimeout(function () { toast.classList.remove("show"); }, 6000); setTimeout(loop, 22000); }, 8000);
  }

  /* ---------- Share ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var d = { title: document.title, url: location.href };
      if (navigator.share) navigator.share(d).catch(function () {}); else { navigator.clipboard && navigator.clipboard.writeText(location.href); b.textContent = "Link copied ✓"; }
    });
  });
})();
