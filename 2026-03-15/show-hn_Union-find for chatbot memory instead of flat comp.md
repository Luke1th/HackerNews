---
title: "Union-find for chatbot memory instead of flat compaction"
type: show-hn
url: https://www.june.kim/union-find-compaction
domain: www.june.kim
published: Sun, 15 Mar 2026 17:57:32 +0000
tags:
  - hackernews
  - show-hn
  - www-june-kim
---

# Union-find for chatbot memory instead of flat compaction

## Story Details
- **Type:** show-hn
- **Domain:** [www.june.kim](https://www.june.kim/union-find-compaction)
- **Published:** Sun, 15 Mar 2026 17:57:32 +0000

## Links
- [Read Story](https://www.june.kim/union-find-compaction)
- [HN Discussion](https://news.ycombinator.com/item?id=https://www.june.kim/union-find-compaction)

## Summary
<p>Every chatbot handles context overflow the same way — summarize everything into one block and throw away the sources. I replaced that with a union-find forest: messages merge into clusters, each cluster has its own summary, and you can trace any summary back to the messages that produced it.<p>Ran seven trials against flat summarization. UF led by 15-18pp on fact recall in every trial. One hit significance (p=0.039), the rest are directional. The interesting finding: flat summaries drop "footnote" facts (cron schedules, webhook paths) because they compete against headline facts for space. Per-cluster summaries don't have that pressure.<p>Code and trial logs: <a href="https://github.com/kimjune01/union-find-compaction" rel="nofollow">https://github.com/kimjune01/union-find-compaction</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47389941">https://news.ycombinator.com/item?id=47389941</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48