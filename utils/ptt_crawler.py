import requests
from bs4 import BeautifulSoup
import sys


def fetch_board_titles(board: str):
    """Fetches titles from the first page of the given PTT board."""
    url = f"https://www.ptt.cc/bbs/{board}/index.html"
    headers = {"User-Agent": "Mozilla/5.0", "Cookie": "over18=1"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [div.text.strip() for div in soup.select("div.title") if div.text.strip()]
    return titles


def main():
    if len(sys.argv) < 2:
        print("Usage: python ptt_crawler.py <board>")
        sys.exit(1)
    board = sys.argv[1]
    titles = fetch_board_titles(board)
    for t in titles:
        print(t)


if __name__ == "__main__":
    main()
