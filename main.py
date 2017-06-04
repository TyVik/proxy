from bs4 import BeautifulSoup
from flask import Flask, Response, request
import requests

from processors import modify_links
from settings import PROXY_SITE, LOG

app = Flask(__name__.split('.')[0])


@app.route('/<path:url>')
def proxy(url):
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
