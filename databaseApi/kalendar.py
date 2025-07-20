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


async def select_daymonth_by_nameday(first_name: str):
    """
    Najde datum(day, month) podle jména.
    Vrací list.
    """
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/GetByName/{first_name}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_nameday_by_daymonth(day, month):
    """
    Najde jména(nameday) podle data.
    Vrací list.
    """
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/GetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_holiday_by_daymonth(day, month):
    """
    Najde svatek(holiday) podle data.
    Vrací list.
    """
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/SvatekGetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json


async def select_fact_by_daymonth(day, month):
    """
    Najde fakt(fact) podle data.
    Vrací list.
    """
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Kalendars/FaktGetByDate/{day},{month}",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json
