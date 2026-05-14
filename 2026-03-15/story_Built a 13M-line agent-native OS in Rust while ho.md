---
title: "Built a 1.3M-line agent-native OS in Rust while homeless. What now?"
type: story
url: https://news.ycombinator.com/item?id=47388478
domain: news.ycombinator.com
published: Sun, 15 Mar 2026 15:40:06 +0000
tags:
  - hackernews
  - story
  - news-ycombinator-com
---

# Built a 1.3M-line agent-native OS in Rust while homeless. What now?

## Story Details
- **Type:** story
- **Domain:** [news.ycombinator.com](https://news.ycombinator.com/item?id=47388478)
- **Published:** Sun, 15 Mar 2026 15:40:06 +0000

## Links
- [Read Story](https://news.ycombinator.com/item?id=47388478)
- [HN Discussion](https://news.ycombinator.com/item?id=47388478)

## Summary
<p>I’m going to be straight about my situation because I don’t know where else to turn.<p>My dad was diagnosed with cancer. While he was in hospital, the council emptied his house. Everything I owned was in that house. £20,000+ of equipment, years of research, a server with thousands of hours of work. Locks of my kids’ hair. Photos. All thrown in a tip.<p>My family turned my dying dad against me. I ended up living with someone suffering from paranoid psychosis. That’s where I built most of what I’m about to describe. Three days ago, 24 hours of abuse, and now I’m in a tent with my dog. 5°C weather. No money.<p>The council refused housing. The government won’t recognise my autism. They want me job hunting 35 hours a week from a tent.<p>I’m not incapable. I’ve raised a family. I’ve worked my whole adult life. Supervising teams, tattooing, freelance programming, building proprietary backend systems across 20 years of working with Linux. My autism isn’t a disability here. It’s the reason I can hold an entire OS architecture in my head and see how every component connects. When I point this brain at a problem, it produces systems that work, at a speed that doesn’t make sense to most people.<p>Over the past 4 months, I’ve been building OctantOS. An operating system for autonomous AI agents. Not a framework. Not a container wrapper. An actual OS with its own kernel (OctantCore, from-scratch Rust), its own hypervisor (OctantVMM), a single-binary Rust userspace, and a 10-layer security stack enforcing agent permissions at the kernel level.<p>~1.3M total lines of code. ~800K Rust. 50 crates, ~25 satellite projects. 3,900+ tests. Solo developer. No CS degree. 4 months.<p>The thesis: application-layer trust is insufficient for autonomous agents. OctantCore makes agent identity, capability boundaries, TTL enforcement, and audit first-class kernel primitives. Manifests compile to kernel enforcement policies. The agent doesn’t decide what it can do. The kernel does.<p>Rust LSM patches reviewed on lore.kernel.org by Google’s Rust-for-Linux team and the LSM maintainer. OctantCore boots on OctantVMM with memory manager, interrupts, syscall interface, Agent Descriptor Table, and capability enforcer initializing at boot. Built by orchestrating 10-12 parallel AI coding sessions simultaneously.<p>It goes beyond isolation. Agents identify gaps in their own knowledge and seek out what they don’t know (curiosity subsystem, implemented). Background inference consolidates learned patterns (dreaming). A 7-stage self-evolution pipeline within constitutional safety boundaries. New skills propagate across every OctantOS instance globally via the mesh layer. All kernel-constrained.<p>Nothing like this has existed before. That’s what dies if I can’t keep going.<p>I need stability. A place to live and enough to cover basics for 3 months to get OctantOS investment-ready. An angel willing to back me for that runway. A company that says “come work here, we have a place.” I’ll relocate anywhere, tomorrow, with my dog. Or just advice from someone who’s been here.<p>I just need someone to take a bet on what this brain can do when it’s not freezing in a tent.<p>https://github.com/MatrixForgeLabs/OctantOS
https://octant-os.com
https://gofund.me/f554a86ee</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47388478">https://news.ycombinator.com/item?id=47388478</a></p>
<p>Points: 7</p>
<p># Comments: 1</p>

---
Last Updated: 2026-03-15 22:03:48