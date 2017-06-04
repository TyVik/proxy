import re

from bs4 import Comment
from flask import request


def modify_links(soup, site):
    for a in soup.findAll('a'):
        link = a.get('href', None)
        if link is not None:
            a['href'] = link.replace(site, request.host_url)
    return soup


def set_tm(text, symbol):
    regex = re.compile(r"\b(\w{6})\b", re.IGNORECASE)
    return regex.sub("\\1" + symbol, text)


def modify_text(soup, symbol, skip_tags):
    for text in soup.findAll(text=True):
        if len(text) > 5 and not isinstance(text, Comment):
            if text.parent is not None and text.parent.name in skip_tags:
                continue
            text.replace_with(set_tm(text, symbol))
    return soup
