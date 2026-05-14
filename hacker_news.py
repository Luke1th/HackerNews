#!/usr/bin/python3
import requests
import json
import datetime
import os
import feedparser
import time
from pathlib import Path

# Obsidian vault path
VAULT_PATH = r"C:\Users\Obsidian_vault"
HN_FOLDER = os.path.join(VAULT_PATH, "HackerNews")

# RSS Feed URLs
RSS_URLS = [
    "https://hnrss.org/newest",
    "https://hnrss.org/show",
    "https://hnrss.org/ask"
]

def create_date_folder():
    """Create a folder with today's date"""
    now = datetime.datetime.now()
    folder_name = now.strftime('%Y-%m-%d')
    folder_path = os.path.join(HN_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def clean_title(title):
    """Clean title for safe file naming"""
    return "".join(x for x in title[:50] if x.isalnum() or x in (' ', '-', '_'))

def fetch_hn_rss():
    """Fetch HackerNews stories from RSS"""
    try:
        folder_path = create_date_folder()
        now = datetime.datetime.now()
        
        # Create daily digest first
        digest_path = os.path.join(folder_path, "00_Daily_Digest.md")
        with open(digest_path, 'w', encoding='utf-8') as f:
            f.write(f"""---
type: hn-digest
date: {now.strftime('%Y-%m-%d')}
tags: [hackernews, digest]
---

# HackerNews Daily Digest - {now.strftime('%Y-%m-%d')}

## 📰 Latest Stories

```dataview
TABLE 
    title as "Title",
    domain as "Source",
    type as "Type"
FROM "HackerNews/{now.strftime('%Y-%m-%d')}"
WHERE type = "story"
SORT file.ctime desc
LIMIT 25
```

## 🏷️ Story Types

```dataview
TABLE WITHOUT ID
    length(rows) as "Count",
    type as "Type"
FROM "HackerNews/{now.strftime('%Y-%m-%d')}"
GROUP BY type
SORT length(rows) DESC
```

## 🌐 Top Domains

```dataview
TABLE WITHOUT ID
    length(rows) as "Stories",
    domain as "Domain"
FROM "HackerNews/{now.strftime('%Y-%m-%d')}"
GROUP BY domain
SORT length(rows) DESC
LIMIT 10
```

Last Updated: {now.strftime('%Y-%m-%d %H:%M:%S')}
""")
        
        print(f"📁 Created daily digest in {os.path.basename(folder_path)}")
        
        # Fetch from multiple RSS feeds
        for rss_url in RSS_URLS:
            print(f"🔄 Fetching from {rss_url}...")
            feed = feedparser.parse(rss_url)
            
            if not feed.entries:
                print(f"⚠️ No entries found in {rss_url}")
                continue
            
            for entry in feed.entries:
                try:
                    # Extract title and determine type
                    title = entry.title
                    story_type = "story"
                    if "Show HN:" in title:
                        story_type = "show-hn"
                        title = title.replace("Show HN:", "").strip()
                    elif "Ask HN:" in title:
                        story_type = "ask-hn"
                        title = title.replace("Ask HN:", "").strip()
                    
                    # Get domain from link
                    url = entry.link
                    domain = url.split('/')[2] if url and len(url.split('/')) > 2 else 'self'
                    
                    content = f"""---
title: "{title}"
type: {story_type}
url: {url}
domain: {domain}
published: {entry.published}
tags:
  - hackernews
  - {story_type}
  - {domain.replace('.', '-')}
---

# {title}

## Story Details
- **Type:** {story_type}
- **Domain:** [{domain}]({url})
- **Published:** {entry.published}

## Links
- [Read Story]({url})
- [HN Discussion](https://news.ycombinator.com/item?id={url.split('=')[-1]})

## Summary
{entry.get('summary', 'No summary available')}

---
Last Updated: {now.strftime('%Y-%m-%d %H:%M:%S')}"""
                
                    # Save story with type prefix for better organization
                    safe_title = clean_title(title)
                    file_path = os.path.join(folder_path, f"{story_type}_{safe_title}.md")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"📰 Saved {story_type}: {title[:50]}...")
                    time.sleep(0.1)  # Small delay between saves
                    
                except Exception as e:
                    print(f"❌ Error processing entry: {e}")
                    continue
        
        print("✅ Completed fetching HackerNews stories")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main execution function"""
    try:
        print("🔄 Starting HackerNews RSS scraper...")
        fetch_hn_rss()
        print("✅ Scraping complete!")
    except Exception as e:
        print(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    main() 