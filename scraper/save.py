"""
Save scraped webpages as JSON.
"""

import json
import os
from urllib.parse import urlparse


def save_json(document):
    """
    Save a scraped document as JSON using a unique filename.
    """

    category = document["category"]
    brand = document["brand"]
    url = document["url"]

    folder = os.path.join("data", "raw", category)
    os.makedirs(folder, exist_ok=True)

    # Extract last part of URL
    path = urlparse(url).path.strip("/")

    if path:
        page_name = path.split("/")[-1]
    else:
        page_name = "home"

    # Clean filename
    page_name = (
        page_name.lower()
        .replace("-", "_")
        .replace("%27", "")
        .replace("%c3%ba", "u")
        .replace("%c3%ab", "e")
    )

    brand_name = (
        brand.lower()
        .replace(" ", "_")
        .replace("'", "")
        .replace("é", "e")
        .replace("ú", "u")
    )

    filename = f"{brand_name}_{page_name}.json"

    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(document, f, indent=4, ensure_ascii=False)

    print(f"✅ Saved: {filepath}")