import asyncio
import aiohttp
from aiohttp import web
from aiohttp.web_request import Request
from bs4 import BeautifulSoup

import processors
from settings import PROXY_SITE, LOG, PROCESSORS, SERVER_PORT, PROXY_URL, SERVER_HOST


async def proxy(request: Request) -> web.Response:
    def prepare_headers(headers):
        headers['host'] = PROXY_SITE
        headers['Accept-Encoding'] = 'deflate'
        return headers

    def response_body(raw: bytes) -> bytes:
        content = raw.decode()
        soup = BeautifulSoup(content, "html.parser")  # OPTIMIZE: use lxml instead html.parser
        for processor, kwargs in PROCESSORS.items():
            func = getattr(processors, processor)
            soup = func(soup, **kwargs)
        return str.encode(str(soup))

    url = '{site}{url}'.format(site=PROXY_URL, url=request.match_info['path'])
    async with aiohttp.ClientSession() as session:
        async with session.request(request.method, url, headers=prepare_headers(request.headers),
                                   params=request.rel_url.query, data=await request.read()) as resp:
            LOG.debug("Got %s response from %s", resp.status, url)
            raw = await resp.read()
            if 'text/html' in resp.headers['Content-Type']:
                # exclude static from parsing
                raw = response_body(raw)
            response = web.Response(body=raw, status=resp.status, headers=resp.headers)
            response.enable_chunked_encoding()
            return response


if __name__ == '__main__':
    app = web.Application()
    app.router.add_route('*', '/{path:.*}', proxy)

    loop = asyncio.get_event_loop()
    f = loop.create_server(app.make_handler(), SERVER_HOST, SERVER_PORT)
    srv = loop.run_until_complete(f)
    print('serving on', srv.sockets[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
