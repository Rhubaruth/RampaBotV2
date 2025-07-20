import aiohttp

from databaseApi import headers_config, ssl_config
from loadEnv import URL_REST_API

# TODO: refactor -- create helper functions for api calls
# -- wrapper_get & wrapper_post


async def select_user_alle():
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/All",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_user_by_name(first_name: str):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/GetByName/{first_name}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_user_by_id(id: int):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/GetById/{id}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_narozky_by_day_month(day, month):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Users/GetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def insert_user(data):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.post(f"{URL_REST_API}Users/New",
                                headers=headers_config(), json=data) as response:
            response_json = await response.json()
    return response_json


async def update_user_by_id(id_user: int, data):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.put(f"{URL_REST_API}Users/Update/{id_user}",
                               headers=headers_config(), json=data) as response:
            response_json = await response.json()
    return response_json
