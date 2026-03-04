#!/usr/bin/env python3
"""Convert markdown files to HTML for GitHub Pages.

Renders all .md files as HTML with clickable links so LLMs using
web fetch tools can navigate the content by following links.
"""

import posixpath
import re
import shutil
from pathlib import Path

import markdown

BASE_URL = "https://initialchicken.github.io/Dodge-Ram-FSM"
EXCLUDE = {".git", ".github", "_site", "__pycache__"}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
{content}
</body>
</html>"""


def convert_md_links(html, file_rel_dir):
    """Rewrite .md hrefs to absolute .html URLs."""
    def replace_link(match):
        rel_href = match.group(1) + ".html"
        if file_rel_dir:
            full_path = posixpath.normpath(posixpath.join(file_rel_dir, rel_href))
        else:
            full_path = posixpath.normpath(rel_href)
        return f'href="{BASE_URL}/{full_path}"'

    return re.sub(r'href="([^"]*?)\.md"', replace_link, html)


def build():
    src = Path(".")
    out = Path("_site")

    if out.exists():
        shutil.rmtree(out)
    out.mkdir()

    md_converter = markdown.Markdown(extensions=["tables", "fenced_code"])

    count = 0
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)

        # Skip excluded directories
        if any(part in EXCLUDE for part in rel.parts):
            continue
        # Skip build script itself and _site output
        if rel.name == "build.py":
            continue

        dest = out / rel

        if path.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)

        if path.suffix == ".md":
            md_converter.reset()
            md_content = path.read_text(encoding="utf-8", errors="replace")
            html_body = md_converter.convert(md_content)
            file_rel_dir = str(rel.parent) if str(rel.parent) != "." else ""
            html_body = convert_md_links(html_body, file_rel_dir)

            # Extract title from first h1, fall back to filename
            m = re.search(r"<h1[^>]*>(.*?)</h1>", html_body)
            title = m.group(1) if m else rel.stem

            html_page = TEMPLATE.format(title=title, content=html_body)

            html_dest = dest.with_suffix(".html")
            html_dest.write_text(html_page, encoding="utf-8")

            # Also copy original .md for direct access
            shutil.copy2(path, dest)
            count += 1
        else:
            shutil.copy2(path, dest)

    print(f"Converted {count} markdown files. Output in {out}/")


if __name__ == "__main__":
    build()
