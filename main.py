from flask import Flask, Response, request
import requests

PROXY_SITE = 'https://habrahabr.ru'

app = Flask(__name__.split('.')[0])


@app.route('/<path:url>')
def proxy(url):
    r = requests.get('{site}{url}'.format(site=PROXY_SITE, url=request.full_path))
    content = r.content
    return Response(content)


if __name__ == '__main__':
    app.run()
