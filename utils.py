# for seen links tracking

SEEN_FILE = "seen_links.txt"

def load_seen_links():
    try:
        with open(SEEN_FILE, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        return set()

def save_seen_links(links):
    with open(SEEN_FILE, "a") as f:
        for link in links:
            f.write(link + "\n")
