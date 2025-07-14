import aiohttp

from Database import headers_config, ssl_config
from envLoad import URL_REST_API


async def select_tournament_all():
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Tournaments/All",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_tournament_today():
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Tournaments/Near",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json
