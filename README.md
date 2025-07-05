# Python Scraper App

This is a Python web scraper that fetches notices from a target URL, filters based on keywords, and sends notifications (e.g., to Discord). The app is designed to run continuously and can be hosted on platforms like Replit.

---

## Features

- Scrapes notices from a specified URL
- Filters notices based on keywords (case-insensitive)
- Sends notifications via Discord webhook
- Runs in a loop with configurable delay (e.g., every 5 minutes)
- Can be hosted 24/7 on Replit with a simple web server and UptimeRobot to prevent sleeping
- Uses environment variables to store sensitive data securely

---

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Environment Variables

Create environment variables for sensitive data:

| Variable Name    | Description                        |
|------------------|----------------------------------|
| `TARGET_URL`     | URL to scrape notices from       |
| `KEYWORDS`       | Comma-separated keywords to filter (e.g. "CSIT,BSc CSIT") |
| `DISCORD_WEBHOOK`| Discord webhook URL for notifications |

On Replit, set these in the Secrets panel (recommended) or in a `.env` file (if Secrets not available).

---

## How to Run Locally

1. Clone the repository
2. Create a `.env` file or set environment variables
3. Install dependencies:

```bash
pip install -r requirements.txt
