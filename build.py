#!/usr/bin/env python3
"""
Personal website generator — Xinyu Li
======================================
Edit the CONTENT dictionary below, then run:

    python build.py

Regenerates index.html, research.html, misc.html from scratch.

Content notes
--------------
* Plain-text fields are HTML-escaped automatically — write normal text.
* "bio" paragraphs accept raw HTML (links live inside them); inserted verbatim.
* Authors: list of (name, is_self) tuples.
* Social links: list of (label, url) tuples — shown after email/CV in contact strip.
  Leave empty [] if you have none yet.
* photo_life: path to the "life side" photo shown on the home page (second card).
"""

import html as _html
import json
import os

# ══════════════════════════════════════════════════════════════════════════════
#  CONTENT  —  edit everything in this section
# ══════════════════════════════════════════════════════════════════════════════

CONTENT = {

    # ── Identity ──────────────────────────────────────────────────────────────
    "name":          "Xinyu Li",
    "name_zh":       "李欣羽",

    # Pronunciation shown on the home page below the Chinese name.
    # X ≈ "sh" in English; ü ≈ German "über" / French "une".
    "pronunciation": "shin-yü lee",

    "email": "xinyu.li@link.cuhk.edu.hk",
    "cv":    "assets/xinyu_cv_2605.pdf",

    # Research-interest tags shown under the name.
    "research_interests": ["IT/AI Innovation", "Open-source Platforms"],

    # One-line education / affiliation shown under the tags.
    "education_line": "PhD candidate @ CUHK DOT · HUST ’22",

    # Connect channels — shown as underlined links under the photo cards.
    # The label is what appears on the page. Add more freely, e.g.
    #   ("Google Scholar", "https://scholar.google.com/..."),
    #   ("SSRN", "https://papers.ssrn.com/..."),
    "social_links": [
        ("LinkedIn", "https://www.linkedin.com/in/xinyuli0108"),
    ],

    # ── Home page photos ──────────────────────────────────────────────────────
    "photo_professional": "assets/profile.png",             # primary card (portrait)
    "photo_life":         "assets/profile-other-side.jpeg", # secondary card (life side)

    # ── Home page — bio paragraphs (raw HTML allowed) ─────────────────────────
    "bio": [
        'I am a fourth-year Ph.D. candidate in the '
        '<a href="https://www.bschool.cuhk.edu.hk/departments/decisions-operations-and-technology/"'
        ' target="_blank" rel="noopener">'
        'Department of Decisions, Operations and Technology at The Chinese University of Hong Kong (CUHK)'
        '</a>, where I am fortunate to be advised by '
        '<a href="https://www.bschool.cuhk.edu.hk/staff/kim-keongtae/"'
        ' target="_blank" rel="noopener">Prof. Keongtae Kim</a>. '
        'I received my Bachelor’s degree in Management Information Systems from '
        'Huazhong University of Science and Technology (HUST).',

        'My research interests lie in open innovation—specifically, '
        '<em>how technical advances, digital infrastructure, and organizational settings '
        'jointly shape how individuals autonomously produce, explore, and innovate '
        'in open digital environments.</em>',

        'This interest is partly personal. I grew up in a small town and got my first '
        'laptop at seven, and what struck me then was access: information that physical '
        'distance had kept out of reach was suddenly available. The waves of IT that '
        'followed—mobile internet, online platforms, and now AI—extended '
        'that access to almost everyone. But the same systems that opened up information '
        'also began to shape what people consume and create. That tension is what I study.',
    ],

    # ── Research page ─────────────────────────────────────────────────────────
    "research_tagline": (
        "How technical advances, digital infrastructure, and organizational settings "
        "jointly shape how individuals produce, explore, and innovate "
        "in open digital environments."
    ),

    "publications": [
        {
            "title":   "Impacts of generative AI on user contributions: evidence from a coding Q&A platform",
            "authors": [("Xinyu Li", True), ("Keongtae Kim", False)],
            "venue":   "Marketing Letters · 2025",
            "link":    ("Paper ↗", "https://doi.org/10.1007/s11002-024-09747-1"),
            "abstract": (
                "This study investigates the short-term impact of generative AI, exemplified by the "
                "introduction of ChatGPT, on user contributions in a coding Q&A platform. We find that "
                "the introduction of ChatGPT led to a reduction in the number of high-quality answers "
                "provided by users, particularly among highly engaged contributors, despite an overall "
                "increase in answers. We identify two key mechanisms: (1) increased perceived "
                "question sophistication despite no actual change in content and (2) reduced "
                "motivation of loyal users in providing answers in the face of AI-generated alternatives. "
                "The findings suggest that while generative AI can facilitate value creation on "
                "user-generated content (UGC) platforms, it also poses challenges in retaining core "
                "contributors and managing content quality. The paper contributes to the literature on "
                "the impact of AI adoption on platforms and suggests practical implications for UGC "
                "platform management, such as the need for AI content disclosure measures to retain "
                "engaged users."
            ),
        },
    ],

    "working_papers": [
        {
            "title":   "Assessing Open Source Software Developer’s Opportunity Costs in a Time of Generative AI",
            "authors": [
                ("Xinyu Li", True),
                ("Francis Joseph Costello", False),
                ("Keongtae Kim", False),
                ("Xiaoquan (Michael) Zhang", False),
            ],
            "venue": "2nd Round R&R · Management Science",
            "link":  ("SSRN ↗", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5100609"),
            "abstract": (
                "Recent advancements in generative artificial intelligence (AI) have paved the way for "
                "tools that can automate knowledge work, with open source software (OSS) development "
                "seeing an influx of AI-based tools for code automation and feedback. These AI tools "
                "have shown promise in increasing productivity. However, less is known about how "
                "developers’ technical activities have changed and whether AI-augmented OSS "
                "development yields personal career benefits. We leverage the March 2023 release of "
                "GitHub Copilot X as a natural experiment, analyzing a 25-week panel dataset of 1,373 "
                "GitHub developers through difference-in-differences with coarsened exact matching. "
                "Furthermore, we augment our GitHub data with individual LinkedIn career trajectories "
                "over 6–12 months post-treatment. We find that developers engage in "
                "“cognitive arbitrage,” experiencing lowered cognitive and time opportunity "
                "costs in development activities, enabling increased sustained and exploratory "
                "development of more varied coding activities. Additionally, heterogeneous analysis "
                "found that casual developers utilized AI more to reduce opportunity costs. "
                "Interestingly, this enhanced development activity translated into increased short to "
                "medium-term career benefits for all developers. Overall, our research suggests that "
                "generative AI fundamentally alters the open innovation equation by removing human "
                "cognitive barriers, allowing developers to assume more creative roles while "
                "simultaneously accelerating their career advancement opportunities."
            ),
        },
        {
            "title":   "Open Boundaries, Quiet Withdrawals: How Cross-Ecosystem Interoperability Reshapes Open-Source AI Ecosystems",
            "authors": [("Xinyu Li", True), ("Miaozhe Han", False)],
        },
        {
            "title":   "Startup Adoption of AI Services and Its Consequences",
            "authors": [("Xinyu Li", True), ("Wen Wen", False), ("Keongtae Kim", False)],
        },
    ],

    # ── Misc page ─────────────────────────────────────────────────────────────
    "misc_intro": (
        "Outside the office, I spend much of my time moving through landscapes that require "
        "more than a laptop. I jog, hike, climb, and trail-run — drawn to the kind of "
        "terrain where elevation and effort are the only metrics that matter. Some of the places "
        "I have been lucky enough to reach: Yubeng Village beneath the Meili Snow Mountain, "
        "the length of Tiger Leaping Gorge, the old streets of Kashgar, and all ten sections "
        "of the MacLehose Trail across Hong Kong. Feel free to reach out if you share the same "
        "impulse to just start walking."
    ),

    "photos": [
        {"src": "assets/kashgar-baisha_lake.jpeg", "alt": "Baisha Lake, Xinjiang",
         "place": "Baisha Lake",    "region": "Kashgar · Xinjiang"},
        {"src": "assets/kashgar-muztagata.jpeg",   "alt": "Muztagh Ata, Xinjiang",
         "place": "Muztagh Ata",    "region": "Xinjiang · 4,688 m"},
        {"src": "assets/maclehose-4.JPG",             "alt": "MacLehose Trail, Hong Kong",
            "place": "MacLehose Trail", "region": "Hong Kong · Section 4"},
        {"src": "assets/maclehose-po-pin-chau.jpeg", "alt": "Po Pin Chau, Hong Kong",
            "place": "Po Pin Chau", "region": "Hong Kong · Sai Kung"},
        {"src": "assets/yubeng-1.jpeg", "alt": "Yubeng Village, Yunnan",
         "place": "Ice Cave", "region": "Yunnan · Sacred Waterfall Trail"},
        {"src": "assets/yubeng-2.jpeg",            "alt": "Yubeng trail, Yunnan",
         "place": "Yubeng Village",         "region": "Yunnan · On the trail"},
        {"src": "assets/yubeng-3.JPG",             "alt": "Yubeng Village, Yunnan",
         "place": "Yubeng Village", "region": "Yunnan · Meili Snow Mountain"},
        {"src": "assets/potatso-national-park.jpeg", "alt": "Potatso National Park, Yunnan",
         "place": "Potatso National Park", "region": "Yunnan · Shangri-La"},
    ],

    # ── Trail map (Leaflet + GPX) ─────────────────────────────────────────────
    #
    # Each trail shows a labeled PIN immediately at (lat, lon).
    # When you add a GPX file, the actual walked ROUTE LINE draws on top.
    #
    # To add a real route:
    #   1. Export the hike as a .gpx file (from Strava, Garmin, AllTrails
    #      recording, Gaia GPS, etc.) — "Export GPX" / "Export original".
    #   2. Drop it into  assets/gpx/  e.g.  assets/gpx/yubeng.gpx
    #   3. Set  "gpx": "assets/gpx/yubeng.gpx"  on that trail below.
    #   4. Run  python build.py  again.
    #
    # lat/lon are rough centers used for the pin + initial framing; tweak freely.
    "trails": [
        {"name": "Yubeng Trek",        "region": "Yunnan · Meili Snow Mountain",
         "lat": 28.434, "lon": 98.801, "gpx": None},
        {"name": "Tiger Leaping Gorge","region": "Yunnan · Upper trail",
         "lat": 27.193, "lon": 100.110, "gpx": None},
        {"name": "Muztagh Ata / Kashgar", "region": "Xinjiang · Karakoram",
         "lat": 38.470, "lon": 75.190, "gpx": None},
        {"name": "MacLehose Trail",    "region": "Hong Kong · Sections 1–10",
         "lat": 22.424, "lon": 114.220, "gpx": None},
        {"name": "Mt. Sanqingshan (三清山)", "region": "Jiangxi",
         "lat": 28.915, "lon": 118.064, "gpx": None},
        {"name": "Qianba Trail (千八线)", "region": "Zhejiang · Longquan",
         "lat": 28.074, "lon": 119.141, "gpx": None},
        {"name": "Mt. Wugong (武功山)", "region": "Jiangxi",
         "lat": 27.459, "lon": 114.150, "gpx": None},
        {"name": "Mt. Huangshan (黄山)", "region": "Anhui",
         "lat": 30.137, "lon": 118.168, "gpx": None},
        {"name": "Mt. Mogan (莫干山)", "region": "Zhejiang · Huzhou",
         "lat": 30.634, "lon": 119.870, "gpx": None},
        {"name": "Mt. Wutong (梧桐山)", "region": "Guangdong · Shenzhen",
         "lat": 22.573, "lon": 114.193, "gpx": None},
        {"name": "Pat Sin Leng (八仙岭)", "region": "Hong Kong · New Territories",
         "lat": 22.499, "lon": 114.186, "gpx": None},
        {"name": "Sunset Peak (大东山)", "region": "Hong Kong · Lantau Island",
         "lat": 22.259, "lon": 113.964, "gpx": None},
    ],
}

# ══════════════════════════════════════════════════════════════════════════════
#  GENERATOR  —  no need to edit below this line
# ══════════════════════════════════════════════════════════════════════════════

_FONTS = (
    "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;"
    "1,400;1,500&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;"
    "1,400;1,500&family=Inter:wght@300;400;500;600&display=swap"
)

e = _html.escape   # escape plain text before inserting into HTML


def _head(title: str, head_extra: str = "") -> str:
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{e(title)}</title>\n'
        '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f'  <link href="{_FONTS}" rel="stylesheet">\n'
        '  <link rel="stylesheet" href="css/style.css">\n'
        + head_extra
        + '</head>\n<body>\n'
    )


def _nav(active: str, c: dict) -> str:
    """Circular avatar logo on the left, page links on the right."""
    pages = [("index.html", "Home"), ("research.html", "Research"), ("misc.html", "Misc")]
    links = "\n".join(
        '        <li><a href="{}"{}>{}</a></li>'.format(
            href, ' class="active"' if name.lower() == active else '', name)
        for href, name in pages
    )
    return (
        '\n  <nav class="site-nav">\n    <div class="nav-inner">\n'
        f'      <a href="index.html" class="nav-logo">\n'
        f'        <img src="assets/logo.jpg" alt="{e(c["name"])}">\n'
        f'      </a>\n'
        f'      <ul class="nav-links">\n{links}\n      </ul>\n'
        '    </div>\n  </nav>\n'
    )


def _footer(c: dict, extra: str = "") -> str:
    return (
        '\n  <footer class="site-footer">\n'
        f'    {e(c["name"])} &nbsp;&middot;&nbsp; CUHK Business School'
        ' &nbsp;&middot;&nbsp; Hong Kong\n'
        '  </footer>\n'
        + extra
        + '\n</body>\n</html>\n'
    )


def _authors_html(authors: list) -> str:
    return ", ".join(
        f'<strong>{e(n)}</strong>' if self else e(n)
        for n, self in authors
    )


def _paper_card(paper: dict) -> str:
    lines = ['<article class="paper-card card">']
    if paper.get("venue"):
        lines.append(f'  <p class="paper-venue">{e(paper["venue"])}</p>')
    lines.append(f'  <h2 class="paper-title">{e(paper["title"])}</h2>')
    lines.append(f'  <p class="paper-authors">{_authors_html(paper["authors"])}</p>')
    if paper.get("abstract") or paper.get("link"):
        lines.append('  <div class="paper-actions">')
        if paper.get("abstract"):
            lines.append(
                '    <button class="abstract-btn" aria-expanded="false">'
                '<span class="caret">&#9660;</span>&ensp;Abstract</button>'
            )
        if paper.get("link"):
            lbl, url = paper["link"]
            lines.append(
                f'    <a href="{e(url)}" class="paper-link"'
                f' target="_blank" rel="noopener">{e(lbl)}</a>'
            )
        lines.append('  </div>')
    if paper.get("abstract"):
        lines.append(
            f'  <div class="abstract-text" role="region">\n'
            f'    {e(paper["abstract"])}\n  </div>'
        )
    lines.append('</article>')
    return "\n".join(lines)


# ── Page builders ──────────────────────────────────────────────────────────────

def _contact_link(text: str, href: str, external: bool) -> str:
    attrs = ' target="_blank" rel="noopener"' if external else ''
    return f'          <a class="contact-link" href="{e(href)}"{attrs}>{e(text)}</a>'


def build_index(c: dict) -> str:
    bio_paras = "\n        ".join(f'<p>{p}</p>' for p in c["bio"])

    # Research-interest tags
    tags_html = "\n".join(
        f'          <span class="hero-tag">{e(t)}</span>'
        for t in c.get("research_interests", [])
    )

    # Contact links — underlined, grouped in a row at the end of the bio column.
    # Email is shown as the address itself with [at] in place of @.
    email_display = c["email"].replace("@", "[at]")
    links = [_contact_link(email_display, f'mailto:{c["email"]}', external=False)]
    for label, url in c.get("social_links", []):
        links.append(_contact_link(label, url, external=True))
    links.append(_contact_link("CV", c["cv"], external=True))
    contact_html = "\n".join(links)

    body = (
        '\n  <main class="page">\n'
        '    <section class="home-hero">\n\n'
        # ── Left column: name → education → tags → bio → contacts ──
        '      <div class="hero-left">\n\n'
        f'        <h1 class="display-name">{e(c["name"])}</h1>\n'
        '        <div class="display-name-sub">\n'
        f'          <span class="display-name-zh">{e(c["name_zh"])}</span>\n'
        f'          <span class="display-pron">{e(c["pronunciation"])}</span>\n'
        '        </div>\n'
        f'        <p class="hero-edu">{e(c["education_line"])}</p>\n\n'
        '        <div class="hero-tags">\n'
        f'{tags_html}\n'
        '        </div>\n\n'
        '        <div class="hero-bio">\n'
        f'          {bio_paras}\n'
        '        </div>\n\n'
        '        <nav class="contact-list" aria-label="Contact and links">\n'
        f'{contact_html}\n'
        '        </nav>\n\n'
        '      </div>\n\n'
        # ── Right column: tilted photo cards ──
        '      <div class="hero-right">\n'
        '        <div class="photo-stack">\n'
        f'          <div class="photo-card photo-card--primary">\n'
        f'            <img src="{e(c["photo_professional"])}"'
        f' alt="Portrait of {e(c["name"])}">\n'
        '          </div>\n'
        f'          <div class="photo-card photo-card--secondary">\n'
        f'            <img src="{e(c["photo_life"])}" alt="Outdoor photo">\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n\n'
        '    </section>\n'
        '  </main>'
    )
    return _head(c["name"]) + _nav("home", c) + body + _footer(c)


def build_research(c: dict) -> str:
    pub_cards = "\n\n    ".join(_paper_card(p) for p in c["publications"])
    wp_cards  = "\n\n    ".join(_paper_card(p) for p in c["working_papers"])
    body = (
        '\n  <main class="page">\n\n'
        '    <header class="page-header">\n'
        '      <p class="eyebrow">Academic Work</p>\n'
        '      <h1>Research</h1>\n'
        '    </header>\n\n'
        f'    <p class="research-tagline">{e(c["research_tagline"])}</p>\n\n'
        '    <div class="divider"><span>Publications &amp; Accepted Papers</span></div>\n\n'
        f'    {pub_cards}\n\n'
        '    <div class="divider"><span>Working Papers &amp; Work in Progress</span></div>\n\n'
        f'    {wp_cards}\n\n'
        '  </main>'
    )
    script = (
        '\n  <script>\n'
        "    document.querySelectorAll('.abstract-btn').forEach(btn => {\n"
        "      btn.addEventListener('click', () => {\n"
        "        const open = btn.classList.toggle('open');\n"
        "        btn.setAttribute('aria-expanded', open);\n"
        "        btn.closest('.paper-card')"
        ".querySelector('.abstract-text').classList.toggle('open');\n"
        "      });\n"
        "    });\n"
        '  </script>\n'
    )
    return _head(f"Research · {c['name']}") + _nav("research", c) + body + _footer(c, extra=script)


_LEAFLET_HEAD = (
    '  <link rel="stylesheet"'
    ' href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"\n'
    '        integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="'
    ' crossorigin="">\n'
    '  <script defer'
    ' src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"\n'
    '          integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="'
    ' crossorigin=""></script>\n'
    '  <script defer'
    ' src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js">'
    '</script>\n'
)


def _trail_map_script(trails: list) -> str:
    """Leaflet map: a pin per trail; GPX route line drawn when a file is set."""
    data = json.dumps(trails)
    # accent red from the palette, used for route lines + pins
    return (
        '\n  <script>\n'
        '  window.addEventListener("load", function () {\n'
        f'    const TRAILS = {data};\n'
        '    const ACCENT = "#C8102E";\n'
        '    if (!window.L) return;\n'
        '\n'
        '    const map = L.map("trail-map", {\n'
        '      scrollWheelZoom: false,\n'
        '      attributionControl: true,\n'
        '    });\n'
        '\n'
        '    // Muted light basemap (CARTO Positron) — fits the cream palette\n'
        '    L.tileLayer(\n'
        '      "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",\n'
        '      { maxZoom: 19, subdomains: "abcd",\n'
        '        attribution: \'&copy; <a href="https://www.openstreetmap.org/copyright">'
        'OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>\' }\n'
        '    ).addTo(map);\n'
        '\n'
        '    const dot = L.divIcon({ className: "trail-dot",\n'
        '      iconSize: [14, 14], iconAnchor: [7, 7], popupAnchor: [0, -8] });\n'
        '\n'
        '    let bounds = L.latLngBounds([]);\n'
        '    function fit() { if (bounds.isValid()) '
        'map.fitBounds(bounds, { padding: [40, 40], maxZoom: 9 }); }\n'
        '\n'
        '    function addPin(t) {\n'
        '      if (t.lat == null) return;\n'
        '      L.marker([t.lat, t.lon], { icon: dot }).addTo(map)\n'
        '        .bindPopup("<b>" + t.name + "</b><br>" + (t.region || ""));\n'
        '      bounds.extend([t.lat, t.lon]);\n'
        '    }\n'
        '\n'
        '    TRAILS.forEach(function (t) {\n'
        '      addPin(t);                       // always show a labeled pin\n'
        '      if (t.gpx) {                     // overlay the real route if present\n'
        '        new L.GPX(t.gpx, {\n'
        '          async: true,\n'
        '          polyline_options: { color: ACCENT, weight: 4, opacity: 0.85 },\n'
        '          marker_options: { startIconUrl: null, endIconUrl: null, shadowUrl: null },\n'
        '        })\n'
        '        .on("loaded", function (e) { bounds.extend(e.target.getBounds()); fit(); })\n'
        '        .addTo(map);\n'
        '      }\n'
        '    });\n'
        '\n'
        '    fit();\n'
        '    if (!bounds.isValid()) map.setView([30, 95], 3);\n'
        '  });\n'
        '  </script>\n'
    )


def build_misc(c: dict) -> str:
    photo_items = []
    for p in c["photos"]:
        photo_items.append(
            f'      <div class="photo-item">\n'
            f'        <img src="{e(p["src"])}" alt="{e(p["alt"])}" loading="lazy">\n'
            f'        <div class="photo-caption">\n'
            f'          <span class="place">{e(p["place"])}</span>\n'
            f'          <span class="region">{e(p["region"])}</span>\n'
            f'        </div>\n'
            f'      </div>'
        )
    photos_html = "\n\n".join(photo_items)

    trails = c.get("trails", [])
    map_section = ""
    map_script = ""
    if trails:
        map_section = (
            '    <div class="divider"><span>Trails Walked</span></div>\n\n'
            '    <div class="trail-map-wrap card">\n'
            '      <div id="trail-map"></div>\n'
            '    </div>\n'
            '    <p class="map-note">Pins mark where I&rsquo;ve been; '
            'lines trace the routes I walked. Scroll-zoom is off &mdash; '
            'drag to pan, use the&nbsp;+&nbsp;/&nbsp;&minus; buttons to zoom.</p>\n\n'
        )
        map_script = _trail_map_script(trails)

    body = (
        '\n  <main class="page">\n\n'
        '    <header class="page-header">\n'
        '      <p class="eyebrow">Beyond the Desk</p>\n'
        '      <h1>Misc</h1>\n'
        '    </header>\n\n'
        f'    <p class="misc-intro">{e(c["misc_intro"])}</p>\n\n'
        f'    <div class="photo-grid">\n\n{photos_html}\n\n    </div>\n\n'
        f'{map_section}'
        '  </main>'
    )
    head_extra = _LEAFLET_HEAD if trails else ""
    return (
        _head(f"Misc · {c['name']}", head_extra=head_extra)
        + _nav("misc", c)
        + body
        + _footer(c, extra=map_script)
    )


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    pages = {
        "index.html":    build_index(CONTENT),
        "research.html": build_research(CONTENT),
        "misc.html":     build_misc(CONTENT),
    }
    for filename, content in pages.items():
        path = os.path.join(here, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓  {filename}")
    print("\nDone. Push to GitHub to deploy.")
