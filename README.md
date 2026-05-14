# HackerNews

Simple script to fetch and display Hacker News RSS items.

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
