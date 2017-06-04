import re
from typing import Iterable

from bs4 import Comment, BeautifulSoup

SYMBOL_REGEXP = re.compile(r"\b(\w{6})\b", re.IGNORECASE)


def modify_links(soup: BeautifulSoup, site: str, host_url: str) -> BeautifulSoup:
    for a in soup.findAll('a'):
        link = a.get('href', None)
        if link is not None:
            a['href'] = link.replace(site, host_url)
    return soup


def set_tm(text: str, symbol: str) -> str:
    return SYMBOL_REGEXP.sub("\\1" + symbol, text)


def modify_text(soup: BeautifulSoup, symbol: str, skip_tags: Iterable[str]) -> BeautifulSoup:
    for text in soup.findAll(text=True):
        if len(text) > 5 and not isinstance(text, Comment):
            if text.parent is not None and text.parent.name in skip_tags:
                continue
            text.replace_with(set_tm(text, symbol))
    return soup
