---
title: "Detach – Mobile UI for managing AI coding agents from your phone"
type: show-hn
url: https://github.com/salvozappa/detach
domain: github.com
published: Sun, 15 Mar 2026 17:40:19 +0000
tags:
  - hackernews
  - show-hn
  - github-com
---

# Detach – Mobile UI for managing AI coding agents from your phone

## Story Details
- **Type:** show-hn
- **Domain:** [github.com](https://github.com/salvozappa/detach)
- **Published:** Sun, 15 Mar 2026 17:40:19 +0000

## Links
- [Read Story](https://github.com/salvozappa/detach)
- [HN Discussion](https://news.ycombinator.com/item?id=https://github.com/salvozappa/detach)

## Summary
<p>Hey guys, about two months ago I started this side-project for "asynchronous coding"
where I can prompt Claude Code from my mobile on train rides, get a notification
when it's done and then review and commit the code from the app itself.<p>Since then I've been using it on and off for a while. I finally decided to polish
it and publish it in case someone might find it useful.<p>It's a self-hosted PWA with four panels: Agent (terminal running Claude Code), Explore (file browser with syntax highlighting), Terminal (standard bash shell), and Git (diff viewer with staging/committing). It can run on a cheap VPS and a fully
functioning setup is provided (using cloud-init and simple bash scripts).<p>This fits my preferred workflow where I stay in the loop: I review every diff, control git manually, and approve or reject changes before they go anywhere.<p>Stack: Go WebSocket bridge, xterm.js frontend, Ubuntu sandbox container. Everything runs in Docker. Works with any CLI AI assistant, though I've only used it with Claude Code.<p>Side project, provided as-is under MIT license. Run at your own risk. Feedback and MRs welcome.<p>EDIT: Removed redundant text</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47389747">https://news.ycombinator.com/item?id=47389747</a></p>
<p>Points: 2</p>
<p># Comments: 2</p>

---
Last Updated: 2026-03-15 22:03:48