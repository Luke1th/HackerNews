---
title: "I Built LiveAuth: POW and Lightning Network Authentication for AI Agents"
type: story
url: https://news.ycombinator.com/item?id=47390942
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 19:25:11 +0000
tags:
  - hackernews
  - story
  - news-ycombinator-com
---

# I Built LiveAuth: POW and Lightning Network Authentication for AI Agents

## Story Details
- **Type:** story
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47390942)
- **Published:** Sun, 15 Mar 2026 19:25:11 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47390942)
- [HN Discussion](https://news.ycombinator.com/item?id=47390942)

## Summary
<p>AI agents need to pay for API calls. Existing auth solutions don't handle this.<p>LiveAuth is a CAPTCHA alternative that:<p>• Uses Proof-of-Work (free for humans) or Lightning payments (for agents)
• Issues JWT tokens on successful verification
• Supports MCP (Model Context Protocol) for AI agents
• Self-hosted, non-custodial Lightning<p>The problem it solves:<p>• CAPTCHAs are broken - AI solves them in seconds
• API keys leak, have no per-request payment
• Agents need identity + ability to pay for resources<p>How it works:<p>1. User/agent requests auth challenge
2. Solves PoW (free) OR pays 1-3 sats via Lightning
3. Gets JWT token valid for API calls
4. Agent can pre-fund a Lightning wallet for autonomous payments<p>Demo: https://docs.liveauth.app/demo.html
Landing page: https://liveauth.app<p>Built with .NET 8, Angular, LND node. Open source coming soon.<p>Questions? AMA.</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390942">https://news.ycombinator.com/item?id=47390942</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48