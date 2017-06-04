from bs4 import BeautifulSoup
from flask import Flask, Response, request
import requests

import processors
from settings import PROXY_SITE, LOG, PROCESSORS

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
        for processor, kwargs in PROCESSORS.items():
            func = getattr(processors, processor)
            soup = func(soup, **kwargs)
        content = str(soup)
    return Response(content)


if __name__ == '__main__':
    app.run()
