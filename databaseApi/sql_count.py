import aiohttp

from Database import ssl_config, headers_config
from envLoad import URL_REST_API


async def select_svatek_count(name):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/GetByNameCount/{name}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_narozky_count(day, month):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/GetByDateCount/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json
