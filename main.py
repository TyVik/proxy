from flask import Flask, Response
import requests

app = Flask(__name__.split('.')[0])


@app.route('/<path:url>')
def proxy(url):
    r = requests.get('https://habrahabr.ru/{}'.format(url))
    content = r.content
    return Response(content)


if __name__ == '__main__':
    app.run()
