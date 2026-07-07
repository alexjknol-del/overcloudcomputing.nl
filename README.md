# overcloudcomputing.nl

Statische website voor Over Cloud Computing, een naslagwerk over cloud computing voor Nederlandse organisaties. Frameworkloos gebouwd met Python en Jinja2, geschikt voor deployment via Cloudflare Pages of GitHub Pages.

## Structuur

```
build.py                 Static site generator
content/guides/          Kennisbankgidsen als markdown met YAML-frontmatter
content/data.py          Begrippenlijst en veelgestelde vragen (voedt tekst en schema)
templates/               Jinja2-templates
static/                  CSS, favicon en assets
public/                  Build-output (wordt gegenereerd, niet in versiebeheer)
```

## Paginatypes

- Home met genummerd register van de hoofdonderdelen
- Cloudmodellen: pijlerpagina over IaaS, PaaS, SaaS en de vormen publiek, privaat, hybride en multicloud
- Kennisbank: genummerde index van gidsen, met detailpagina's
- Begrippenlijst: definities met DefinedTermSet-schema
- Veelgestelde vragen: accordeon met FAQPage-schema
- Contact, privacybeleid, cookiebeleid

## Lokaal bouwen

```bash
pip install -r requirements.txt
python build.py
cd public && python -m http.server 8000
```

## Nieuwe gids toevoegen

Plaats een markdown-bestand in `content/guides/` met frontmatter:

```markdown
---
title: "Titel van de gids"
description: "Korte omschrijving voor zoekmachines en previews."
date: 2026-07-01
category: "Migratie"
reading_time: 5
---

De inhoud in markdown.
```

De bestandsnaam bepaalt de URL: `cloudmigratie-in-fasen.md` wordt `/kennisbank/cloudmigratie-in-fasen/`.

## Begrippen of vragen aanpassen

De begrippenlijst en de vragenpagina komen uit `content/data.py`. Aanpassingen daar verschijnen automatisch in zowel de zichtbare pagina als de bijbehorende JSON-LD.

## Deployment via Cloudflare Pages

### A. Bouwen op Cloudflare (aanbevolen)

- Build command: `pip install -r requirements.txt && python build.py`
- Build output directory: `public`
- Python-versie via omgevingsvariabele `PYTHON_VERSION`, bijvoorbeeld `3.12`

### B. Vooraf bouwen en committen

Verwijder `public/` uit `.gitignore`, voer lokaal `python build.py` uit, commit de map, en stel in Cloudflare Pages het build command leeg in met output directory `public`.

## Domein

Productie: `https://overcloudcomputing.nl`. Pas `SITE["url"]` in `build.py` aan bij een domeinwijziging; die waarde bepaalt de canonical-tags en de sitemap.
