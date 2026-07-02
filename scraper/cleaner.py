"""
Text cleaning utilities.
"""

import re


def clean_text(text):
    """
    Clean scraped webpage text.
    """

    text = re.sub(r"\s+", " ", text)

    return text.strip()