import aiohttp
from databaseApi import ssl_config, headers_config
from loadEnv import URL_REST_API


async def get_async(url: str):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}{url}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def post_async(url: str, data_dict):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.post(f"{URL_REST_API}{url}",
                                headers=headers_config(),
                                json=data_dict) as response:
            response_json = await response.json()
    return response_json


async def put_async(url: str, data_dict):
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.put(f"{URL_REST_API}{url}",
                               headers=headers_config(),
                               json=data_dict) as response:
            response_json = await response.json()
    return response_json
