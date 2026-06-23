---
name: run-bharatcalc
description: Build, serve, screenshot, and smoke-test the BharatCalc static calculator site. Use when asked to run, start, serve, preview, screenshot, or verify BharatCalc or any of its calculator/article pages locally.
---

# Run BharatCalc

BharatCalc is a **static HTML site** — no build, no framework, no npm at the
project level (Tailwind via CDN, vanilla JS per page). You "run" it by serving
the folder over HTTP and driving it with headless **system Chrome** via
`playwright-core`. The driver lives at
`.claude/skills/run-bharatcalc/driver.mjs` and does both screenshots and a
calculator smoke test.

All paths below are relative to the project root (`D:\Work\Tools\BharatCalc`).

## Prerequisites

- **Python 3** (for the static server) and **Node 18+** — both already present.
- **Google Chrome** installed (the driver uses `channel: 'chrome'`, so no
  browser download). Verified at
  `C:\Program Files\Google\Chrome\Application\chrome.exe`.

One-time driver dependency install (no browser download):

```bash
cd .claude/skills/run-bharatcalc
PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install --no-audit --no-fund
```

`node_modules/` and `*.png` are gitignored inside the skill dir.

## Run (agent path) — START HERE

**1. Serve the site** (background) from the project root:

```bash
python -m http.server 8000 --bind 127.0.0.1 >/tmp/httpd.log 2>&1 &
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8000/   # expect 200
```

**2. Drive it** with the driver (server must already be running):

```bash
cd .claude/skills/run-bharatcalc

# Smoke test: drives the SIP calculator, asserts the corpus recomputes
node driver.mjs --smoke

# Screenshot any page (full page) — pass a BARE path, no leading slash
node driver.mjs calculator/emi-calculator.html emi.png
node driver.mjs "" home.png      # no path => homepage
```

`--smoke` changes Monthly Investment 10,000 → 25,000 and asserts
`#corpusResult` changes (₹50.46L → ₹1.26Cr) with no console errors. Exit code
is non-zero on failure. Screenshots are written next to the driver; open them
to confirm fonts/Tailwind/charts rendered.

Override defaults with env vars: `BASE_URL` (default
`http://127.0.0.1:8000`), `CHROME` (explicit Chrome exe path, bypasses
`channel:'chrome'`).

## Run (human path)

Open the served URL in a normal browser:
`http://127.0.0.1:8000/` then navigate. Or just double-click any `.html` —
pages mostly work from `file://` too, but the canonical/OG tags and the
manifest assume the served origin, so prefer the server.

## Test

There is no unit-test suite. The smoke test (`node driver.mjs --smoke`) is the
verification path. For a new calculator, screenshot it and confirm a value
change recomputes its result element.

## Gotchas

- **Git Bash mangles leading-slash args.** Running `node driver.mjs /` makes
  MSYS rewrite `/` into `C:/Program Files/Git/`, so the driver would request
  `http://127.0.0.1:8000/C:/Program%20Files/Git/` → 404. Pass **bare paths**
  (`calculator/sip-calculator.html`, or `""` for home). The driver also
  detects and rewrites the mangled value back to `/` as a safety net.
- **Server must be running before the driver.** The driver does not start it.
  If you see `status 404` / connection refused, (re)launch `python -m
  http.server` from the project root and re-check with curl.
- **The navbar/footer logo is `favicon.svg`** — a 256×256 PNG embedded as
  base64 inside an SVG (~29 KB), used via `<img src=".../favicon.svg">`. It's
  the only `<img>` on the site; everything else (card/section icons) is inline
  `<svg>`. It renders fine; don't mistake its size for breakage.
- **`site.webmanifest` serves locally as `application/octet-stream`** under
  `python -m http.server`. Harmless; PWA icons still resolve.
- The background server keeps running across turns. Stop it with
  `taskkill //F //IM python3.13.exe` (or kill the specific PID) when done.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Driver: `status 404`, page is `/C:/Program%20Files/Git/...` | Git Bash mangled a `/` arg — use a bare path, no leading slash. |
| Driver: connection refused / 404 on a real page | Server not running or wrong CWD. Start `python -m http.server 8000` **from the project root**, verify with curl. |
| `Cannot find package 'playwright-core'` | Run the install step in `.claude/skills/run-bharatcalc`. |
| Chrome launch fails / channel not found | Set `CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"` before the node command. |
