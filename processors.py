import re

from bs4 import Comment
from flask import request

from settings import PROXY_SITE, SKIP_TAG, SYMBOL


def modify_links(soup):
    for a in soup.findAll('a'):
        link = a.get('href', None)
        if link is not None:
            a['href'] = link.replace("{}/".format(PROXY_SITE), request.host_url)
    return soup


def set_tm(text, symbol):
    regex = re.compile(r"\b(\w{6})\b", re.IGNORECASE)
    return regex.sub("\\1" + symbol, text)


def modify_text(soup):
    for text in soup.findAll(text=True):
        if len(text) > 5 and not isinstance(text, Comment):
            if text.parent is not None and text.parent.name in SKIP_TAG:
                continue
            text.replace_with(set_tm(text, SYMBOL))
    return soup
