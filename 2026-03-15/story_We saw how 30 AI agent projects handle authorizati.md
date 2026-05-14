---
title: "We saw how 30 AI agent projects handle authorization-93% use unscoped API keys"
type: story
url: https://news.ycombinator.com/item?id=47388873
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 16:19:37 +0000
tags:
  - hackernews
  - story
  - news-ycombinator-com
---

# We saw how 30 AI agent projects handle authorization-93% use unscoped API keys

## Story Details
- **Type:** story
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47388873)
- **Published:** Sun, 15 Mar 2026 16:19:37 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47388873)
- [HN Discussion](https://news.ycombinator.com/item?id=47388873)

## Summary
<p>We reviewed 30 of the most popular AI agent projects on GitHub (OpenClaw,
  AutoGen, CrewAI, LangGraph, MetaGPT, AutoGPT, etc.) across six authorization
  criteria: scoped permissions, per-agent identity, user consent, revocation,
  audit trails, and delegation control.<p><pre><code>  Key findings:
  - 93% rely on unscoped API keys as the only auth mechanism
  - 0% have per-agent cryptographic identity
  - 97% have no user consent flow
  - 100% have no per-agent revocation

  We mapped the gaps to OWASP's Agentic Top 10 (ASI01, ASI03, ASI05, ASI09,
  ASI10) and documented real incidents from this year — 21k exposed OpenClaw
  instances, 492 MCP servers with zero auth, 1.5M leaked tokens in the
  Moltbook breach.

  Full report: https://grantex.dev/report/state-of-agent-security-2026</code></pre></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47388873">https://news.ycombinator.com/item?id=47388873</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48