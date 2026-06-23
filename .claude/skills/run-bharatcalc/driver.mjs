#!/usr/bin/env node
// BharatCalc run-driver. Drives the static site with headless system Chrome
// via playwright-core (no bundled browser download — uses channel: 'chrome').
//
// Usage (server must already be running, see SKILL.md):
//   node driver.mjs <path> [outPng]   navigate to BASE+<path>, screenshot, report console errors
//   node driver.mjs --smoke           drive the SIP calculator, assert the corpus recomputes
//
// Env:
//   BASE_URL  default http://127.0.0.1:8000
//   CHROME    explicit Chrome executable path (overrides channel:'chrome')

import { chromium } from 'playwright-core';

const BASE = process.env.BASE_URL || 'http://127.0.0.1:8000';

const launchOpts = { headless: true };
if (process.env.CHROME) launchOpts.executablePath = process.env.CHROME;
else launchOpts.channel = 'chrome';

async function withPage(fn) {
  const browser = await chromium.launch(launchOpts);
  const page = await browser.newPage({ viewport: { width: 1280, height: 1800 } });
  const errors = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  try {
    return await fn(page, errors);
  } finally {
    await browser.close();
  }
}

function normalizePath(path) {
  // Git Bash (MSYS) rewrites a bare leading-slash arg ("/") into a Windows
  // path like "C:/Program Files/Git/". Treat that as the site root.
  if (!path || /Program Files[\\/]Git/.test(path)) return '/';
  return path.startsWith('/') ? path : '/' + path;
}

async function screenshot(path, outPng = 'shot.png') {
  return withPage(async (page, errors) => {
    const url = BASE + normalizePath(path);
    const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.screenshot({ path: outPng, fullPage: true });
    const title = await page.title();
    console.log(`status   ${resp.status()}`);
    console.log(`title    ${title}`);
    console.log(`shot     ${outPng}`);
    console.log(`console  ${errors.length ? errors.join(' | ') : 'no errors'}`);
    if (resp.status() !== 200) process.exitCode = 1;
  });
}

async function smoke() {
  return withPage(async (page, errors) => {
    await page.goto(BASE + '/calculator/sip-calculator.html', { waitUntil: 'networkidle', timeout: 30000 });
    const read = () => page.locator('#corpusResult').innerText();
    const before = await read();
    // change monthly investment 10000 -> 25000 and fire the input event the page listens for
    await page.fill('#monthlyInput', '25000');
    await page.dispatchEvent('#monthlyInput', 'input');
    await page.waitForTimeout(300);
    const after = await read();
    await page.screenshot({ path: 'smoke.png', fullPage: true });
    console.log(`corpus before  ${before}`);
    console.log(`corpus after   ${after}`);
    console.log(`console        ${errors.length ? errors.join(' | ') : 'no errors'}`);
    if (before === after) {
      console.error('FAIL: corpus did not recompute after changing input');
      process.exitCode = 1;
    } else {
      console.log('PASS: corpus recomputed on input change');
    }
  });
}

const [a, b] = process.argv.slice(2);
if (a === '--smoke') await smoke();
else await screenshot(a || 'index.html', b); // no arg => homepage
