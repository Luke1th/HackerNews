---
title: "Deathwatch, a CLI to detect abandoned dependencies"
type: show-hn
url: https://github.com/davitotty/deathwatch
domain: github.com
published: Sun, 15 Mar 2026 19:11:20 +0000
tags:
  - hackernews
  - show-hn
  - github-com
---

# Deathwatch, a CLI to detect abandoned dependencies

## Story Details
- **Type:** show-hn
- **Domain:** [github.com](https://github.com/davitotty/deathwatch)
- **Published:** Sun, 15 Mar 2026 19:11:20 +0000

## Links
- [Read Story](https://github.com/davitotty/deathwatch)
- [HN Discussion](https://news.ycombinator.com/item?id=https://github.com/davitotty/deathwatch)

## Summary
<p>Show HN: deathwatch – CLI to detect abandoned dependencies (npm + pip)<p>I got tired of discovering mid-project that a package hadn't been touched in years. deathwatch scans your package.json and/or requirements.txt and flags deps that are dead, suspicious, or healthy before they become a problem.
bashnpm install -g deathwatch
deathwatch
It checks last publish date, weekly download count (flags if under 100/week), and deprecated notices on npm. PyPI support too. Everything is color-coded in the terminal, no config needed.
Tune sensitivity with flags:
bashdeathwatch --threshold 12 --warn 6
Source: <a href="https://github.com/davitotty/deathwatch" rel="nofollow">https://github.com/davitotty/deathwatch</a>
npm: <a href="https://www.npmjs.com/package/deathwatch" rel="nofollow">https://www.npmjs.com/package/deathwatch</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390793">https://news.ycombinator.com/item?id=47390793</a></p>
<p>Points: 2</p>
<p># Comments: 1</p>

---
Last Updated: 2026-03-15 22:03:48