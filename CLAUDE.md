# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

BharatCalc is a static HTML calculator site targeting Indian users, optimized for SEO. No framework — every page is a standalone `.html` file using compiled Tailwind CSS (`/styles.css`) and vanilla JS. The goal is to publish many calculators fast while keeping design and SEO consistent.

**CSS build:** Tailwind is compiled once into `/styles.css` (not loaded at runtime — the old `cdn.tailwindcss.com` script was removed for Core Web Vitals). After adding/changing any Tailwind classes in HTML, regenerate the stylesheet:

```
npm install         # one-time
npm run build:css   # rebuild /styles.css after editing markup
```

Theme (colors/fonts) lives in `tailwind.config.js`; content globs already cover `*.html`, `calculator/*.html`, `articles/*.html`. Every page links `<link rel="stylesheet" href="/styles.css" />` plus a small per-page `<style>` block for custom components.

Live site: `https://bharatcalc.online/`  
Analytics: Google Analytics (`G-9TD6B9GQ89`)

## Project Structure

```
index.html               — homepage with search, category tabs, and all calculator cards
sitemap.xml              — manually maintained; update when adding a calculator
robots.txt               — static
calculator/*.html        — one file per calculator
about.html / privacy.html / terms.html
logo.png / logo-round.png
calculator-template.md   — operating manual (read this before any new calculator work)
```

## Adding a New Calculator — Checklist

Every new calculator requires ALL of the following. Do not skip steps:

1. Create `calculator/<name>-calculator.html` — follow the structure of an existing calculator like `sip-calculator.html`
2. Add a card to `index.html` (in the correct category section, JS `calcs` array)
3. Add a `<url>` entry to `sitemap.xml` with today's date, `changefreq: monthly`, `priority: 0.8`
4. Link to it from exactly 4 related calculators (and update those calculators' "Related" sections to link back)

## Calculator Page Structure (required order)

1. `<head>` — SEO meta: unique `<title>`, `<meta name="description">`, `<link rel="canonical">`, OG tags, Twitter card
2. Two JSON-LD blocks: `WebApplication` schema (with breadcrumb) + `FAQPage` schema
3. `<link rel="stylesheet" href="/styles.css" />` (copy the head block from any existing calculator). Do NOT re-add the `cdn.tailwindcss.com` script. After adding markup with new Tailwind classes, run `npm run build:css`.
4. Google Analytics script (copy from any existing calculator — same GA ID)
5. Navbar (copy from any existing calculator — identical across all pages)
6. H1 + calculator interface
7. Formula section
8. Explanation section with example
9. FAQ section (minimum 5 questions, using `<details>`/`<summary>` accordion pattern)
10. Related calculators — exactly 4 cards
11. Footer (copy from any existing calculator)

## Design System

Colors (Tailwind custom palette — never change):
- `ink` — dark blue-grey scale, `ink-900` = `#0d1117` (body text / dark bg)
- `leaf` — green scale, `leaf-600` = `#16a34a` (primary CTA, active states)
- `saffron` — orange scale, `saffron-600` = `#ea580c` (accent)

Fonts (via Google Fonts CDN):
- `font-display` → Clash Display (headings)
- `font-sans` → Satoshi (body)
- `font-mono` → JetBrains Mono (numbers/code)

UI patterns already established — do not invent new ones. Reuse input styles, card styles, button styles, result boxes exactly as seen in existing calculators.

## index.html — How the Calculator Grid Works

The homepage uses a `calcs` JS array. Each entry looks like:
```js
{ name: "SIP Calculator", url: "calculator/sip-calculator.html", cat: "finance", tags: ["sip","mutual fund","..."], icon: "<svg>..." }
```
Category tabs filter by the `cat` field. Valid categories: `finance`, `tax`, `health`, `math`, `tools`.  
Search works against `name` + `tags`. Always add relevant search tags.

## SEO Conventions

- Canonical URL format: `https://bharatcalc.online/calculator/<name>-calculator.html`
- Title format: `<Calculator Name> India – <Benefit> | BharatCalc`
- Meta description: 140–160 chars, include "free", "India", and the primary keyword
- H1 must be unique and match search intent (not just the tool name)
- FAQ schema must mirror the visible FAQ section exactly
- Breadcrumb: Home → Category → Calculator Name

## Current Calculator Inventory (22 calculators)

**Finance:** SIP, EMI, Lumpsum, CAGR, FD, RD, PPF, EPF, NPS, Compound Interest  
**Tax:** Income Tax, GST, HRA, TDS, Gratuity, Advance Tax  
**Health:** BMI, Calorie, Ideal Weight, Due Date  
**Math/Tools:** Percentage, Age

## Planned Next Batch (discussed 2026-06-09)

High-priority (high Indian search volume, natural fit):
- In-Hand Salary Calculator (CTC → take-home)
- Step-up SIP Calculator
- Capital Gains Tax Calculator (STCG/LTCG)
- Home Loan Eligibility Calculator

Also in pipeline:
- Simple Interest Calculator
- SSY (Sukanya Samriddhi Yojana) Calculator
- SCSS (Senior Citizens Savings Scheme) Calculator
- NSC Calculator
- New vs Old Tax Regime Comparator
- Loan Prepayment / Foreclosure Calculator
- Credit Card Interest Calculator
- TDEE Calculator
- Discount Calculator
- Unit Converter
