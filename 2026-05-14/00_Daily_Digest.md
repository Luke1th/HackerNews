---
type: hn-digest
date: 2026-05-14
tags: [hackernews, digest]
---

# HackerNews Daily Digest - 2026-05-14

## 📰 Latest Stories

```dataview
TABLE 
    title as "Title",
    domain as "Source",
    type as "Type"
FROM "HackerNews/2026-05-14"
WHERE type = "story"
SORT file.ctime desc
LIMIT 25
```

## 🏷️ Story Types

```dataview
TABLE WITHOUT ID
    length(rows) as "Count",
    type as "Type"
FROM "HackerNews/2026-05-14"
GROUP BY type
SORT length(rows) DESC
```

## 🌐 Top Domains

```dataview
TABLE WITHOUT ID
    length(rows) as "Stories",
    domain as "Domain"
FROM "HackerNews/2026-05-14"
GROUP BY domain
SORT length(rows) DESC
LIMIT 10
```

Last Updated: 2026-05-14 14:56:20
