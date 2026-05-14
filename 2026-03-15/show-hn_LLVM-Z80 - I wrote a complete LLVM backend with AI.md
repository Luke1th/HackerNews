---
title: "LLVM-Z80 - I wrote a complete LLVM backend with AI"
type: show-hn
url: https://github.com/llvm-z80/llvm-z80
domain: github.com
published: Sun, 15 Mar 2026 19:22:04 +0000
tags:
  - hackernews
  - show-hn
  - github-com
---

# LLVM-Z80 - I wrote a complete LLVM backend with AI

## Story Details
- **Type:** show-hn
- **Domain:** [github.com](https://github.com/llvm-z80/llvm-z80)
- **Published:** Sun, 15 Mar 2026 19:22:04 +0000

## Links
- [Read Story](https://github.com/llvm-z80/llvm-z80)
- [HN Discussion](https://news.ycombinator.com/item?id=https://github.com/llvm-z80/llvm-z80)

## Summary
<p>Two years ago, I started a project called Rust-GB to compile Rust for the Game Boy.<p>At the time, no stable LLVM backend supported the Game Boy’s CPU.<p>I had to use a complex workaround: transpiling Rust to C via LLVM-CBE and then compiling that C code using SDCC.<p>Back then, building a native LLVM backend was a dream, but I lacked the time to do it alone.<p>Fast forward two years, and things have changed.<p>With the help of LLMs, I have successfully implemented a complete LLVM-Z80 backend, including subtarget support for the Game Boy's SM83.<p>In terms of performance, it generally outperforms SDCC, though it currently produces larger binary sizes.<p>While there are still some latent bugs and upstream LLVM core issues to address, 
I’ve successfully compiled most C programs and the entire Rust core library.<p>I’d love to hear your feedback or any questions regarding the backend!<p>- LLVM-Z80: <a href="https://github.com/llvm-z80/llvm-z80" rel="nofollow">https://github.com/llvm-z80/llvm-z80</a> / Rust-Z80: <a href="https://github.com/llvm-z80/rust-z80" rel="nofollow">https://github.com/llvm-z80/rust-z80</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47390920">https://news.ycombinator.com/item?id=47390920</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>

---
Last Updated: 2026-03-15 22:03:48