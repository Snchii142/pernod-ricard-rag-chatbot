from urllib.parse import urlparse


def get_filename(url):
    """
    Create a filename from URL.
    """

    domain = urlparse(url).netloc.replace("www.", "")

    return domain.replace(".", "_") + ".json"