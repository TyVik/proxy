import logging

PROXY_SITE = 'habrahabr.ru'
PROXY_URL = 'https://{}/'.format(PROXY_SITE)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
SERVER_URL = 'http://{host}:{port}/'.format(host=SERVER_HOST, port=SERVER_PORT)

SYMBOL = '™'
SKIP_TAG = ('head', 'meta', 'style', 'body', 'html', 'script', '[document]')

PROCESSORS = {
    'modify_links': {'site': PROXY_URL, 'host_url': SERVER_URL},
    'modify_text': {'symbol': '™', 'skip_tags': ('head', 'meta', 'style', 'body', 'html', 'script', '[document]')}
}


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("PROXY: ")
