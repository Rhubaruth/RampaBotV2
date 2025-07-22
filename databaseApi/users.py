import aiohttp

from databaseApi import headers_config, ssl_config
from loadEnv import URL_REST_API

from databaseApi import wrappers

# TODO: refactor -- create helper functions for api calls
# -- wrapper_get & wrapper_post


async def select_user_all():
    url = "Users/All"
    response_json = await wrappers.get_async(url)
    return response_json


async def select_user_by_name(first_name: str):
    url = f"Users/GetByName/{first_name}"
    response_json = await wrappers.get_async(url)
    return response_json


async def select_user_by_id(id: int):
    url = f"Users/GetById/{id}"
    response_json = await wrappers.get_async(url)
    return response_json


async def select_user_by_daymonth(day, month):
    url = f"Users/GetByDate/{day},{month}"
    response_json = await wrappers.get_async(url)
    return response_json


async def insert_user(data):
    url = "Users/New"
    response_json = await wrappers.post_async(url, data)
    return response_json


async def update_user_by_id(id: int, data):
    print(f'id: {id}, data: {data}')
    url = f"Users/Update/{id}"
    response_json = await wrappers.put_async(url, data)
    return response_json
