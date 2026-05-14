# HackerNews

Simple script to fetch and display Hacker News RSS items.
The scraper fetch information from the links below, create a folder with today's date in Obsidian, creates a daily digest and save the storied with type prefix for better organization.

- https://hnrss.org/newest", 
- "https://hnrss.org/show", 
- "https://hnrss.org/ask" 

<p align="center">
<img width="745" height="344" alt="C2_Delay" src="https://github.com/Luke1th/HackerNews/blob/main/Hacker_news.png" />
</p>

Prerequisites
- Python 3.8 or newer
- A virtual environment (recommended)
- feedparser

Install

PowerShell (from workspace root):

```powershell
& .\Self-learning\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run

```powershell
cd HackerNews
python hacker_news.py
```

Troubleshooting
- If you see "ModuleNotFoundError: No module named 'feedparser'", ensure you're using the venv python and installed `requirements.txt`.
