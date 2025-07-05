# sends message to discord

import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_to_discord(notices):
    for notice in notices:
        title = notice["title"]
        url = notice["url"]

        message = {
            "content": f"📢 **New BSc CSIT Notice**\n📄 {title}\n🔗 {url}"
        }

        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=message)
            response.raise_for_status()
            print(f"[✅] Sent to Discord: {title}")
        except requests.exceptions.RequestException as e:
            print(f"[❌] Failed to send to Discord: {e}")
