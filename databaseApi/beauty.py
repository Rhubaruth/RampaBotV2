import aiohttp

from databaseApi import headers_config, ssl_config
from loadEnv import URL_REST_API

'''
GET->
{
  "id": 0,
  "user_One": 0,
  "user_Two": 0,
  "user_Three": 0
}
'''


async def select_beauty_today():
    async with aiohttp.ClientSession(connector=ssl_config()) as session:
        async with session.get(f"{URL_REST_API}Beauty",
                               headers=headers_config()) as response:
            response_json = await response.json()
    return response_json
