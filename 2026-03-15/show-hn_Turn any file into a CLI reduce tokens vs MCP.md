---
title: "Turn any file into a CLI (reduce tokens vs. MCP)"
type: show-hn
url: https://news.ycombinator.com/item?id=47390978
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 19:28:48 +0000
tags:
  - hackernews
  - show-hn
  - news-ycombinator-com
---

# Turn any file into a CLI (reduce tokens vs. MCP)

## Story Details
- **Type:** show-hn
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47390978)
- **Published:** Sun, 15 Mar 2026 19:28:48 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47390978)
- [HN Discussion](https://news.ycombinator.com/item?id=47390978)

## Summary
<p>I built a tool called clifast.<p>It reads your TypeScript/JavaScript exported functions and generates a complete npm/npx CLI package in one command:<p>npx clifast your-file.ts<p>It parses types, JSDoc comments and function signatures to generate a --help command which can be used by LLMs to navigate the available input arguments and use your files or repositories effectively with less input tokens.<p>Multiple exports become subcommands. External imports are bundled. The output is a ready-to-publish npm package (which comes with the benefits of npx).<p>The goal is to reduce token usage by exposing files or entire folders as CLI commands that can be executed by Claude Code or Cloudflare's Codemode using a reduced amount of input tokens while decreasing the need to build and maintain complex MCP servers when not needed.<p>Repo:
<a href="https://github.com/AlexandrosGounis/clifast" rel="nofollow">https://github.com/AlexandrosGounis/clifast</a><p>Can you please give me some feedback if you find this helpful?</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390978">https://news.ycombinator.com/item?id=47390978</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48