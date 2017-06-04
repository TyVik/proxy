import logging

PROXY_SITE = 'https://habrahabr.ru'
SYMBOL = '™'
SKIP_TAG = ('head', 'meta', 'style', 'body', 'html', 'script', '[document]')

PROCESSORS = {
    'modify_links': {'site': PROXY_SITE + '/'},
    'modify_text': {'symbol': '™', 'skip_tags': ('head', 'meta', 'style', 'body', 'html', 'script', '[document]')}
}


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("PROXY: ")
