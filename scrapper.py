# fetch and filters notices


import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import certifi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
KEYWORDS = [k.strip().lower() for k in os.getenv("KEYWORDS").split(",")]

def fetch_notices():
    try:
        response = requests.get(TARGET_URL, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        notices = []

        # Find all notice blocks
        post_blocks = soup.select("div.recent-post-wrapper.shadow")

        for block in post_blocks:
            link_tag = block.select_one("div.detail a")
            if not link_tag:
                continue

            title = link_tag.get_text(strip=True)
            href = link_tag.get("href")

            if not title or not href:
                continue

            # Match CSIT-related keywords
            if any(kw in title.lower() for kw in KEYWORDS):
                full_url = href if href.startswith("http") else f"https://iost.tu.edu.np{href}"
                notices.append({
                    "title": title,
                    "url": full_url
                })

        return notices

    except Exception as e:
        print(f"[ERROR] Failed to fetch or parse notices: {e}")
        return []
