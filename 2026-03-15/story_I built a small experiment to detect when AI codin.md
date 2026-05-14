---
title: "I built a small experiment to detect when AI coding assistants drift"
type: story
url: https://news.ycombinator.com/item?id=47388616
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 15:56:12 +0000
tags:
  - hackernews
  - story
  - news-ycombinator-com
---

# I built a small experiment to detect when AI coding assistants drift

## Story Details
- **Type:** story
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47388616)
- **Published:** Sun, 15 Mar 2026 15:56:12 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47388616)
- [HN Discussion](https://news.ycombinator.com/item?id=47388616)

## Summary
<p>I recently encountered a common problem while coding with Cursor.<p>Initially, we usually give the AI   some explicit constraints, such as:<p>Don't modify the database schema<p>Don't modify certain APIs<p>Only allow modifications to the front-end logic<p>Some function names cannot be changed<p>At the beginning of the conversation, the AI   generally follows these rules well.<p>However, as the conversation lengthens, for example, to 40,000 or 50,000 tokens, a common problem arises:<p>The AI   gradually "forgets" the previously mentioned restrictions.<p>For example:<p>Initially you say "Don't modify the database,"<p>but after a few rounds, it suddenly suggests:<p>"We can solve this problem by modifying the database structure."<p>I've asked others how to solve this before, and some suggested:<p>Write an important.md or rule file in the project so the AI   reads it every time.<p>This method does have some effect, but problems still arise in actual development.<p>For example:
Initially you say "Don't touch database A,"<p>but later database B is added to the project.<p>If you don't update the markdown file in time, the AI   might accidentally modify things you didn't intend to change.<p>So I recently created a small experimental tool, mainly to solve the "constraint drift" problem in AI programming assistants.</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47388616">https://news.ycombinator.com/item?id=47388616</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48