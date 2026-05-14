---
title: "OpenLegion – AI agent fleet with container isolation and vault proxy"
type: show-hn
url: https://www.openlegion.ai
domain: www.openlegion.ai
published: Sun, 15 Mar 2026 18:41:37 +0000
tags:
  - hackernews
  - show-hn
  - www-openlegion-ai
---

# OpenLegion – AI agent fleet with container isolation and vault proxy

## Story Details
- **Type:** show-hn
- **Domain:** [www.openlegion.ai](https://www.openlegion.ai)
- **Published:** Sun, 15 Mar 2026 18:41:37 +0000

## Links
- [Read Story](https://www.openlegion.ai)
- [HN Discussion](https://news.ycombinator.com/item?id=https://www.openlegion.ai)

## Summary
<p>I built OpenLegion because every AI agent framework I tried had the same problems in production: API keys sitting in config files inside the agent's environment, no way to set hard spend limits, and LLM-as-CEO task routing that's non-deterministic and unauditable.<p>The short version of what I built:<p>Security: Every agent runs in its own Docker container or microVM. A vault proxy sits between agents and every LLM call — the agent sends a request, the proxy injects the credential at the network layer, the agent gets back a response. Keys never exist inside the container. Six independent security layers on by default, including per-agent ACL matrices and Unicode sanitization to block invisible-character prompt injection.<p>Cost control: Per-agent daily and monthly budgets with a hard cutoff enforced at the vault proxy. The agent physically cannot make an LLM call that exceeds its budget. Zero markup on LLM usage — you pay your provider directly at their rates. 100+ providers via LiteLLM with configurable failover chains.<p>Orchestration: Deterministic YAML DAG workflows. No LLM deciding what runs next. Four patterns: sequential, parallel, supervisor, hierarchical. Every execution path is predictable and auditable.<p>The rest: Camoufox stealth browser (C++-level anti-detection, CAPTCHA solving), persistent per-agent vector+BM25 memory with temporal decay, MCP tool support, real-time fleet dashboard, Telegram/Discord/Slack/WhatsApp channels, cron + webhook triggering, agents can write and hot-reload their own Python skills at runtime.<p>The engine is ~30,000 lines of Python with 2,100+ tests. Self-hosted runs on one machine — no Redis, no Kubernetes, just Python 3.10+, Docker, and an API key. Three commands to start.<p>For context: the dominant framework in this space is OpenClaw (200K+ stars). CVE-2026-25253 was reported in February — critical RCE, 42,000 exposed instances with no authentication, 341 malicious skills confirmed stealing user data. I'm not trying to replace it, but that's why I think this gap exists.<p>We launched in February 2026. Zero CVEs. BSL 1.1 license — source-available, not open source, and I want to be clear about that. Managed hosting starts at $19/month with a 7-day free trial. Self-hosted is free.<p>Happy to get specific about the security model or architecture — genuinely curious where people think the threat model breaks down.<p><a href="https://openlegion.ai" rel="nofollow">https://openlegion.ai</a> | <a href="https://docs.openlegion.ai" rel="nofollow">https://docs.openlegion.ai</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390443">https://news.ycombinator.com/item?id=47390443</a></p>
<p>Points: 2</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48