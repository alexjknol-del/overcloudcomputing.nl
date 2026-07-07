#!/usr/bin/env python3
"""Static site generator voor overcloudcomputing.nl.

Frameworkloos: Jinja2 + python-markdown. Gidsen zijn markdown met
YAML-frontmatter in content/guides/. Begrippen en vragen komen uit
content/data.py. Output in public/, geschikt voor Cloudflare Pages.
"""

import shutil
import sys
from datetime import datetime, date
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "content"))
from data import TERMS, FAQS  # noqa: E402

TEMPLATES = ROOT / "templates"
GUIDES = ROOT / "content" / "guides"
STATIC = ROOT / "static"
OUTPUT = ROOT / "public"

SITE = {
    "name": "Over Cloud Computing",
    "url": "https://overcloudcomputing.nl",
    "description": "Onafhankelijk naslagwerk over cloud computing voor Nederlandse organisaties.",
}

NAV = [
    {"label": "Home", "url": "/"},
    {"label": "Cloudmodellen", "url": "/cloudmodellen/"},
    {"label": "Kennisbank", "url": "/kennisbank/"},
    {"label": "Begrippen", "url": "/begrippen/"},
    {"label": "Vragen", "url": "/veelgestelde-vragen/"},
    {"label": "Contact", "url": "/contact/"},
]

MONTHS_NL = ["januari", "februari", "maart", "april", "mei", "juni",
             "juli", "augustus", "september", "oktober", "november", "december"]

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True, lstrip_blocks=True,
)
md = markdown.Markdown(extensions=["extra", "sane_lists"])


def nl_date(d):
    return f"{d.day} {MONTHS_NL[d.month - 1]} {d.year}"


def anchor(term):
    return "term-" + "".join(c for c in term.lower() if c.isalnum())


def load_guides():
    out = []
    for path in sorted(GUIDES.glob("*.md")):
        post = frontmatter.load(path)
        d = post["date"]
        if isinstance(d, datetime):
            d = d.date()
        md.reset()
        out.append({
            "slug": path.stem,
            "title": post["title"],
            "description": post["description"],
            "category": post.get("category", "Gids"),
            "reading_time": post.get("reading_time", 5),
            "date": d,
            "date_display": nl_date(d),
            "date_iso": d.isoformat(),
            "url": f"/kennisbank/{path.stem}/",
            "html": md.convert(post.content),
        })
    out.sort(key=lambda g: g["date"], reverse=True)
    return out


def write(rel_path, html):
    out = OUTPUT / rel_path.lstrip("/")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")


def render(template, page_path, active, **ctx):
    return env.get_template(template).render(
        site=SITE, nav=NAV, active=active, page_path=page_path,
        year=datetime.now().year, legal_date=nl_date(date.today()), **ctx,
    )


def related_for(guide, guides, count=3):
    others = [g for g in guides if g["slug"] != guide["slug"]]
    return others[:count]


def build():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    shutil.copytree(STATIC, OUTPUT / "static")

    guides = load_guides()
    terms = [{"term": t, "definition": d, "anchor": anchor(t)} for t, d in TERMS]

    write("/", render("home.html", "/", "/", latest=guides[:4]))
    write("/cloudmodellen/", render("cloudmodellen.html", "/cloudmodellen/", "/cloudmodellen/"))
    write("/kennisbank/", render("kennisbank.html", "/kennisbank/", "/kennisbank/", guides=guides))
    write("/begrippen/", render("begrippen.html", "/begrippen/", "/begrippen/", terms=terms))
    write("/veelgestelde-vragen/", render("veelgestelde-vragen.html", "/veelgestelde-vragen/", "/veelgestelde-vragen/", faqs=FAQS))
    write("/contact/", render("contact.html", "/contact/", "/contact/"))
    write("/privacybeleid/", render("privacybeleid.html", "/privacybeleid/", None))
    write("/cookiebeleid/", render("cookiebeleid.html", "/cookiebeleid/", None))

    for g in guides:
        write(g["url"], render("guide.html", g["url"], "/kennisbank/",
                               guide=g, related=related_for(g, guides)))

    write_sitemap(guides)
    write_robots()
    print(f"Gebouwd: {len(guides)} gidsen, {len(terms)} begrippen, {len(FAQS)} vragen. Output in {OUTPUT}")


def write_sitemap(guides):
    urls = ["/", "/cloudmodellen/", "/kennisbank/", "/begrippen/",
            "/veelgestelde-vragen/", "/contact/", "/privacybeleid/", "/cookiebeleid/"]
    urls += [g["url"] for g in guides]
    today = date.today().isoformat()
    lastmod = {g["url"]: g["date_iso"] for g in guides}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines += ["  <url>", f"    <loc>{SITE['url']}{u}</loc>",
                  f"    <lastmod>{lastmod.get(u, today)}</lastmod>", "  </url>"]
    lines.append("</urlset>")
    (OUTPUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_robots():
    (OUTPUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build()
