# main scheduler.

import time
import schedule
from scrapper import fetch_notices
# from scraper import fetch_notices
from notifier import send_to_discord
from utils import load_seen_links, save_seen_links

def job():
    print("🔄 Checking for new CSIT notices...")
    seen_links = load_seen_links()
    new_notices = fetch_notices()

    # Filter only unseen notices
    fresh_notices = [n for n in new_notices if n["url"] not in seen_links]

    if fresh_notices:
        send_to_discord(fresh_notices)
        new_links = [n["url"] for n in fresh_notices]
        save_seen_links(new_links)
    else:
        print("✅ No new CSIT notices found.")

# Run every 5 minutes
schedule.every(5).minutes.do(job)

print("🚀 TU CSIT Scraper App started! Checking every 5 minutes...\n")

# Initial run immediately
job()

# Keep the app running
while True:
    schedule.run_pending()
    time.sleep(1)
