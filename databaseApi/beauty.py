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
    """
    Returns list of ids of random members
    """
    response_json = await wrappers.get_async(url="Beauty")
    response_list = [
        {"id": response_json["user_One"]},
        {"id": response_json["user_Two"]},
        {"id": response_json["user_Three"]},
    ]
    return response_list
