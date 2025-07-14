import ssl

import aiohttp

from loadEnv import REST_API_KEY


def ssl_config():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    return conn


def headers_config():
    headers = {
        "Authorization": f"Bearer {REST_API_KEY}",
        "Content-Type": "application/json"
    }
    return headers
