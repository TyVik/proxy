from flask import Flask, Response, request
import logging
import requests

PROXY_SITE = 'https://habrahabr.ru'

app = Flask(__name__.split('.')[0])
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("main.py")


@app.route('/<path:url>')
def proxy(url):
    url = '{site}{url}'.format(site=PROXY_SITE, url=request.full_path)
    r = requests.get(url)
    LOG.debug("Got %s response from %s", r.status_code, url)
    content = r.content
    return Response(content)


if __name__ == '__main__':
    app.run()
