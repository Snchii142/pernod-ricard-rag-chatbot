"""
Web scraper for Pernod Ricard RAG Knowledge Base
"""

import cloudscraper
import time

from bs4 import BeautifulSoup
from scraper.cleaner import clean_text


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}
scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "darwin",
        "mobile": False,
    }
)


def scrape_page(item, category):

    url = item["url"]
    brand = item["brand"]
    source = item["source"]

    try:

        response = scraper.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        title = (
            soup.title.text.strip()
            if soup.title
            else "No Title"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        text = clean_text(text)

        time.sleep(2)

        return {

            "title": title,

            "url": url,

            "brand": brand,

            "category": category,

            "source": source,

            "text": text

        }

    except Exception as e:

        print(f"Error scraping {url}")

        print(e)

        return None