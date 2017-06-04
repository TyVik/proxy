from flask import request

from settings import PROXY_SITE


def modify_links(soup):
    for a in soup.findAll('a'):
        link = a.get('href', None)
        if link is not None:
            a['href'] = link.replace("{}/".format(PROXY_SITE), request.host_url)
    return soup
