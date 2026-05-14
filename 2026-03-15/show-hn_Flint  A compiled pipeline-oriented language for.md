---
title: "Flint – A compiled, pipeline-oriented language for CLI tooling"
type: show-hn
url: https://codeberg.org/lucaas-d3v/flint
domain: codeberg.org
published: Sun, 15 Mar 2026 17:33:15 +0000
tags:
  - hackernews
  - show-hn
  - codeberg-org
---

# Flint – A compiled, pipeline-oriented language for CLI tooling

## Story Details
- **Type:** show-hn
- **Domain:** [codeberg.org](https://codeberg.org/lucaas-d3v/flint)
- **Published:** Sun, 15 Mar 2026 17:33:15 +0000

## Links
- [Read Story](https://codeberg.org/lucaas-d3v/flint)
- [HN Discussion](https://news.ycombinator.com/item?id=https://codeberg.org/lucaas-d3v/flint)

## Summary
<p>Hi HN, I'm Lucas.<p>I write a lot of infrastructure tooling and got frustrated with the usual trilemma: Bash gets unmaintainable past 50 lines, Python's interpreter startup/bloat feels too heavy for fast pipeline tasks, and Rust/Go can be too verbose for simple OS-level scripting.<p>So I built Flint. It’s an experimental, statically-typed language written in Zig that transpiles directly to C99, compiling down to a dependency-free native binary. It is strictly designed for DevOps, SRE, and CLI automation.<p>Some of the core engineering decisions:<p>1. The Pipeline Operator (~>): Data flows forward. No nested function hell. It’s functional composition mapped to C.
2. Memory Model: Zero garbage collection and zero `malloc` churn. It uses a 4GB virtual arena via `mmap(MAP_NORESERVE)`. Scripts boot instantly and die cleanly.
3. Zero-Copy Strings: Strings are fat pointers (ptr + len). Operations like `split()` or `lines()` are just memory slicing, which drastically speeds up parsing large logs or JSONs.
4. OS-Level I/O: We bypass User Space bottlenecks where possible. The `copy()` function delegates directly to the `sendfile` syscall. Process orchestration uses `posix_spawnp` instead of expensive `fork()` cloning.
5. Explicit Errors: Inspired by Zig, I/O operations require an explicit `catch |err|` block. No silent Bash failures.<p>A quick example of what a log parser looks like:
```flint
const raw_logs = read_file("server_access.log") catch |err| { exit(1); };<p>raw_logs
    ~> to_str()
    ~> lines()
    ~> grep("403 FORBIDDEN")
    ~> join("\n")
    ~> write_file("threat_report.log") catch |err| { exit(1); };<p>```<p>Trade-offs & Current State (v1.7.1):
It is NOT a general-purpose language. It lacks a garbage collector by design (long-running daemons will eventually exhaust the arena). I'm currently working on a deep-walk semantic analyzer to enforce proper namespace isolation for the upcoming v1.7.2.<p>I would love brutal feedback on the architecture, specifically the Zig-to-C99 transpilation pipeline and the arena implementation in the C runtime.<p>Repo: <a href="https://codeberg.org/lucaas-d3v/flint" rel="nofollow">https://codeberg.org/lucaas-d3v/flint</a>
Mirror: <a href="https://github.com/lucaas-d3v/flint" rel="nofollow">https://github.com/lucaas-d3v/flint</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=47389657">https://news.ycombinator.com/item?id=47389657</a></p>
<p>Points: 1</p>
<p># Comments: 1</p>

---
Last Updated: 2026-03-15 22:03:48