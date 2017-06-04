import logging

PROXY_SITE = 'https://habrahabr.ru'
SYMBOL = '™'
SKIP_TAG = ('head', 'meta', 'style', 'body', 'html', 'script', '[document]')


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("PROXY: ")
