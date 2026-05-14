---
title: "ARISE – Agents that create their own tools at runtime when they fail"
type: show-hn
url: https://github.com/abekek/arise
domain: github.com
published: Sun, 15 Mar 2026 19:35:10 +0000
tags:
  - hackernews
  - show-hn
  - github-com
---

# ARISE – Agents that create their own tools at runtime when they fail

## Story Details
- **Type:** show-hn
- **Domain:** [github.com](https://github.com/abekek/arise)
- **Published:** Sun, 15 Mar 2026 19:35:10 +0000

## Links
- [Read Story](https://github.com/abekek/arise)
- [HN Discussion](https://news.ycombinator.com/item?id=https://github.com/abekek/arise)

## Summary
<p>I built a framework that lets LLM agents create their own tools at runtime. Most agent frameworks assume you'll hand-craft every tool upfront. That works until your agent hits something you didn't plan for. ARISE (Adaptive Runtime Improvement through Self-Evolution) lets agents synthesize their own tools at runtime when they detect gaps<p>ARISE sits between your agent and its tool library. When the agent keeps failing at a class of tasks, it analyzes what's missing, uses a cheap LLM to synthesize a new Python function, tests it in a sandbox with adversarial edge cases, and if it passes, promotes it. The agent picks it up on the next run. Over time, the agent accumulates tools shaped by the actual tasks it encounters, not just what you imagined at build time.<p>There's a bunch of research on this idea — VOYAGER did it in Minecraft, LATM (LLMs as Tool Makers) showed LLMs can write reusable tools, CRAFT and CREATOR explored similar directions. But none of them resulted in something you can actually pip install and use with your own agent. That's what I'm trying to build.<p>For safety, generated code undergoes sandboxed execution, auto-generated tests, and adversarial validation before entering the active library. Everything is versioned with rollback. I don't fully trust it yet for unsupervised production use, but it's getting there.<p>By default, everything runs locally with SQLite. For deployment, there's a distributed mode where the agent is stateless — it reads skills from a remote store and reports trajectories to a queue. A separate worker process picks those up and runs evolution independently. So you can scale the agent without worrying about evolution blocking your hot path. I tested this end-to-end with real infra and real LLM calls.<p>Works with any agent that takes a task and returns a result. Native Strands adapter, raw OpenAI/Anthropic function calling works too.<p>This is very early — just shipped it. There's a lot to improve. Would really appreciate feedback and contributions if this is interesting to you.</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47391045">https://news.ycombinator.com/item?id=47391045</a></p>
<p>Points: 3</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48