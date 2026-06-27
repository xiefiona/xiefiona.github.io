#!/usr/bin/env python3
"""
Import publications from Semantic Scholar into _data/publications.yml.

Usage (in GitHub Actions):
  - Provide env var S2_AUTHOR_ID (required)
  - Optional: S2_API_KEY for higher rate limits

Writes a grouped-by-year YAML file suitable for the site's pub-list include.
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List

import requests
import yaml

API = "https://api.semanticscholar.org/graph/v1"


def fetch_author_pubs(author_id: str, api_key: str | None = None) -> Dict[str, Any]:
    fields = (
        "papers.title,papers.year,papers.venue,"
        "papers.externalIds,papers.url,papers.authors.name"
    )
    url = f"{API}/author/{author_id}"
    headers = {"User-Agent": "pub-importer/1.0"}
    if api_key:
        headers["x-api-key"] = api_key
    r = requests.get(url, params={"fields": fields, "limit": 1000}, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()


def to_yaml(publications: List[Dict[str, Any]]) -> str:
    # Group by year desc; entries within year sorted by title
    by_year: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for p in publications:
        year = p.get("year") or 0
        by_year[int(year)].append(p)

    grouped = []
    for year in sorted(by_year.keys(), reverse=True):
        items = sorted(by_year[year], key=lambda x: (x.get("venue") or "", x.get("title") or ""))
        yentry = {"year": int(year) if year != 0 else datetime.now().year, "entries": []}
        for it in items:
            links = {}
            ext = it.get("externalIds") or {}
            if it.get("url"):
                links["pdf"] = it["url"]
            if ext.get("DOI"):
                links["doi"] = f"https://doi.org/{ext['DOI']}"
            if ext.get("ArXiv"):
                links["code"] = f"https://arxiv.org/abs/{ext['ArXiv']}"

            authors = ", ".join(a.get("name", "").strip() for a in (it.get("authors") or []))
            yentry["entries"].append(
                {
                    "title": it.get("title", "").strip(),
                    "authors": authors,
                    "venue": (it.get("venue") or "").strip(),
                    "links": links,
                }
            )
        grouped.append(yentry)

    # Use safe_dump for clean YAML without aliases
    return yaml.safe_dump(grouped, sort_keys=False, allow_unicode=True)


def main() -> int:
    author_id = os.environ.get("S2_AUTHOR_ID")
    if not author_id:
        print("S2_AUTHOR_ID is required", file=sys.stderr)
        return 2
    api_key = os.environ.get("S2_API_KEY")
    data = fetch_author_pubs(author_id, api_key)
    papers = data.get("papers", [])
    yaml_text = to_yaml(papers)

    out_path = os.path.join("_data", "publications.yml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    print(f"Wrote {out_path} with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

