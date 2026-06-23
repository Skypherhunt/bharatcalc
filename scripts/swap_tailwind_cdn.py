#!/usr/bin/env python3
"""Replace the runtime Tailwind CDN script + inline config with a compiled
stylesheet link across all HTML pages. One-time migration helper."""
import re
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

files = (
    glob.glob(os.path.join(ROOT, "*.html"))
    + glob.glob(os.path.join(ROOT, "calculator", "*.html"))
    + glob.glob(os.path.join(ROOT, "articles", "*.html"))
)

# preconnect hint to the CDN host — no longer needed
preconnect = re.compile(
    r'[ \t]*<link rel="preconnect" href="https://cdn\.tailwindcss\.com"[^>]*>\s*\n'
)

# the CDN <script> followed immediately by the inline tailwind.config <script>
block = re.compile(
    r'<script src="https://cdn\.tailwindcss\.com"></script>\s*'
    r'<script>\s*tailwind\.config\s*=\s*\{.*?</script>',
    re.DOTALL,
)

LINK = '<link rel="stylesheet" href="/styles.css" />'

changed = 0
for f in files:
    with open(f, encoding="utf-8") as fh:
        src = fh.read()
    if 'href="/styles.css"' in src:
        continue  # already migrated
    new = preconnect.sub("", src, count=1)
    new, n = block.subn(LINK, new, count=1)
    if n != 1:
        print(f"WARN: CDN block not found in {f}")
        continue
    if new != src:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new)
        changed += 1

print(f"Updated {changed} files")
