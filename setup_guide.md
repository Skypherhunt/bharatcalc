# BharatCalc SEO Setup Guide

## Goal
Create lightweight, SEO-friendly calculator pages that rank well on Google and scale easily.

---

# 1. File Structure

Use this structure for every calculator page:

```txt
bharatcalc/
│
├── index.html
│
├── calculator/
│   ├── emi-calculator.html
│   ├── sip-calculator.html
│   ├── gst-calculator.html
│   └── fd-calculator.html
```

---

# 2. SEO Basics For Every Calculator Page

Every calculator page MUST include:

- SEO title
- Meta description
- Proper heading structure
- Mobile responsiveness
- Internal links
- Useful content below calculator
- Fast loading speed

---

# 3. SEO Title

Add inside <head>

Example:

```html
<title>EMI Calculator India - Calculate Loan EMI Online | BharatCalc</title>
```

Rules:
- Include main keyword
- Mention India if relevant
- Keep under 60 characters
- Add brand name at end

---

# 4. Meta Description

Add inside <head>

Example:

```html
<meta name="description" content="Free EMI Calculator for India. Calculate monthly loan EMI, total interest, and total payment instantly with BharatCalc.">
```

Rules:
- 140–160 characters
- Explain page clearly
- Include keyword naturally
- Make users want to click

---

# 5. Heading Structure

Use clean heading hierarchy.

Example:

```html
<h1>EMI Calculator</h1>

<h2>Calculate Your Loan EMI</h2>

<h2>What is EMI?</h2>

<h2>How EMI is Calculated</h2>

<h2>EMI Formula</h2>

<h2>Frequently Asked Questions</h2>
```

Rules:
- Only ONE h1 per page
- Use multiple h2 sections
- Add keywords naturally
- Keep headings readable

---

# 6. Calculator Section

Every calculator page should include:

- Input fields
- Calculate button
- Results section
- Clean UI
- Mobile-friendly layout

Example inputs:
- Loan amount
- Interest rate
- Tenure

Example outputs:
- Monthly EMI
- Total interest
- Total payment

---

# 7. SEO Content Below Calculator

After the calculator UI, add content sections.

Recommended sections:

- What is EMI?
- EMI Formula
- How EMI Works
- Benefits of EMI
- EMI Example Calculation
- FAQ
- Related Calculators

Purpose:
- Helps SEO
- Adds keywords naturally
- Increases page relevance
- Improves ranking potential

---

# 8. Internal Linking

Every page should link to:

- Homepage
- Related calculators

Example:

```html
<a href="/index.html">Home</a>
<a href="/calculator/sip-calculator.html">SIP Calculator</a>
```

Purpose:
- Better crawling
- Better SEO structure
- Higher engagement

---

# 9. URL Structure

Use clean SEO-friendly URLs.

Good:

```txt
/calculator/emi-calculator
/calculator/sip-calculator
```

Bad:

```txt
/page1
/tool123
/calc
```

---

# 10. Performance Rules

Always keep pages:

- lightweight
- fast-loading
- mobile-first
- simple

Avoid:
- heavy frameworks
- unnecessary animations
- bloated JavaScript
- large images

Goal:
Fast pages = better SEO.

---

# 11. Homepage Requirements

Homepage should include:

- Hero section
- Calculator categories
- Popular calculators
- Internal links
- Trustworthy design
- Mobile responsiveness

Purpose:
- Help users navigate
- Improve internal linking
- Improve SEO authority

---

# 12. Deployment Workflow

Workflow:

```txt
Generate page
↓
Add SEO basics
↓
Test responsiveness
↓
Deploy to Vercel
↓
Index on Google
```

---

# 13. Important Long-Term Rule

Do NOT overengineer early.

Main priority:
- Publish useful calculators fast
- Scale pages consistently
- Improve gradually over time

This is an SEO publishing business, not a complex web app.

