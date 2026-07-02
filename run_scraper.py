print("Program Started")

from scraper.urls import URLS
from scraper.scraper import scrape_page
from scraper.save import save_json


def main():

    for category, pages in URLS.items():

        print(f"\n📂 Scraping category: {category}")

        for page in pages:

            document = scrape_page(page, category)

            if document:
                save_json(document)


if __name__ == "__main__":
    main()