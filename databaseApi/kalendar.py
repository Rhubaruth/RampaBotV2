import aiohttp

from databaseApi import headers_config, ssl_config
from loadEnv import URL_REST_API

'''
GET->
[
  {
    "den": 0,
    "mesic": 0,
    "jmeno": "string",
    "svatek": "string"
  }
]
'''


async def select_date_by_name(first_name: str):  # vybere zvolene jmeno z kalendare, vysledek vraci jako list
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/GetByName/{first_name}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_date_by_day_month_jmeno(day, month):  # vybere zvoleny den v kalendari, vysledek vraci jako list
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/GetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_date_by_day_month_svatek(day, month):  # vybere zvoleny den v kalendari, vysledek vraci jako list
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/SvatekGetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_date_by_day_month_fakt(day, month):  # vybere zvoleny den v kalendari, vysledek vraci jako list
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/FaktGetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json
