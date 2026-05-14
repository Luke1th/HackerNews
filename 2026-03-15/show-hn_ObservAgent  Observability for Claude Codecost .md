---
title: "ObservAgent – Observability for Claude Code(cost, tools, subagents)"
type: show-hn
url: https://darshannere.github.io/observagent/
domain: darshannere.github.io
published: Sun, 15 Mar 2026 20:18:36 +0000
tags:
  - hackernews
  - show-hn
  - darshannere-github-io
---

# ObservAgent – Observability for Claude Code(cost, tools, subagents)

## Story Details
- **Type:** show-hn
- **Domain:** [darshannere.github.io](https://darshannere.github.io/observagent/)
- **Published:** Sun, 15 Mar 2026 20:18:36 +0000

## Links
- [Read Story](https://darshannere.github.io/observagent/)
- [HN Discussion](https://news.ycombinator.com/item?id=https://darshannere.github.io/observagent/)

## Summary
<p>I've been running a lot of Claude Code sessions lately: multi-agent workflows, long autonomous runs, and kept hitting the same problem: the session finishes and you have no idea what happened.
   Why did it cost $4? Which tool took 10 seconds? When did the subagent silently fail?<p>Caude writes JSONL transcripts but they're not usable in real time.<p>So I built ObservAgent. It's a local dashboard that gives you live visibility into every Claude
Code session without touching your code.<p>How it works:<p>Claude Code has a hooks system (PreToolUse, PostToolUse, SubagentStart, SubagentStop). ObservAgent installs a tiny Python relay that fires a fire-and-forget POST to a local Fastify server on every hook event. The server stores events in SQLite and streams them to a React dashboard over SSE.<p>npm install -g @darshannere/observagent
observagent init   
# installs hooks into ~/.claude/settings.json
observagent start  
# opens dashboard at localhost:4999<p>That's it. Run any Claude Code session and watch it live.<p>What you get:<p>- Real-time tool call log with latency per call
- Cost tracking 
— token usage per model (including cache read/write) auto-calculated against current Claude pricing
- Agent tree 
— session + subagent hierarchy with per-agent cost rollups
- Session history grouped by repository with one-click replay and JSONL/CSV export
- Health panel with p50/p95 latency and error rates<p>Everything binds to 127.0.0.1. No cloud, no telemetry, no API keys needed.<p>GitHub:<a href="https://github.com/darshannere/observagent" rel="nofollow">https://github.com/darshannere/observagent</a>
npm: npm install -g @darshannere/observagent<p>Happy to answer questions about the hooks architecture or how I handle cost attribution across subagents (trickier than it sounds).</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47391414">https://news.ycombinator.com/item?id=47391414</a></p>
<p>Points: 2</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48