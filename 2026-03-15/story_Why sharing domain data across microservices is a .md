---
title: "Why sharing domain data across microservices is a silent killer"
type: story
url: https://news.ycombinator.com/item?id=47390041
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 18:06:18 +0000
tags:
  - hackernews
  - story
  - news-ycombinator-com
---

# Why sharing domain data across microservices is a silent killer

## Story Details
- **Type:** story
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47390041)
- **Published:** Sun, 15 Mar 2026 18:06:18 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47390041)
- [HN Discussion](https://news.ycombinator.com/item?id=47390041)

## Summary
<p>I spent a few years working at a company where all our microservices backed into MongoDB instances. We were constantly under top-down pressure to deliver fast, and because MongoDB is schemaless, it felt very easy to just add fields to our documents whenever we needed to expose data to another service. We eventually arrived at what we thought was a genius optimization. We wrote a background script to propagate changes from Collection A in one service to another service database. That way, the second service would not need any code modification to see the data it needed.<p>Every time I remember that I still feel bad for not pushing back. We created an unclear interface that coupled our domains together. The second service became dependent on the internal document structure of the first, yet it had no contract to enforce that structure. We chose that path because it was the fastest way to hit our sprint goals. We let the immediate pressure win, and in doing so, we essentially guaranteed that both maintainer teams would be locked in a fragile, entangled dance for the foreseeable future.<p>I have since learned that sharing domain data across boundaries is a recipe for disaster. It is a classic example of prioritizing speed in the present while ignoring the mounting cost of coupling. The better approach should've been to respect domain boundaries and only connect them using a unique immutable identifier instead of sharing stateful objects or duplicating documents. By passing an ID, you maintain the independence of each service so they are free to evolve at their own pace, as long as they don't break the interfaces.</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390041">https://news.ycombinator.com/item?id=47390041</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48