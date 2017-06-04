from bs4 import BeautifulSoup
from flask import Flask, Response, request
import logging
import requests

PROXY_SITE = 'https://habrahabr.ru'

app = Flask(__name__.split('.')[0])
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("main.py")


@app.route('/<path:url>')
def proxy(url):
    def modify_links(soup):
        for a in soup.findAll('a'):
            link = a.get('href', None)
            if link is None:
                LOG.debug('Broken link on page %s', url)
                continue
            a['href'] = link.replace("{}/".format(PROXY_SITE), request.host_url)
        return soup

    url = '{site}{url}'.format(site=PROXY_SITE, url=request.full_path)
    r = requests.get(url)
    LOG.debug("Got %s response from %s", r.status_code, url)
    content = r.content
    if 'text/html' in r.headers['Content-Type']:
        # exclude static from parsing
        soup = BeautifulSoup(content.decode(), "html.parser")  # OPTIMIZE: use lxml instead html.parser
        content = str(modify_links(soup))
    return Response(content)


if __name__ == '__main__':
    app.run()
