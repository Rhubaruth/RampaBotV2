from databaseApi import wrappers

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
    response_json = await wrappers.get_async(url="Beauty")
    return response_json
