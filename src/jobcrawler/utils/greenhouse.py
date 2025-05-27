# Utils for ATS Greenhouse

from lxml import html, etree

def extract_listings(content: bytes | str) -> dict:
    tree = html.fromstring(content)

    return {}