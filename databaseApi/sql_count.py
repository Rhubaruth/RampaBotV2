from databaseApi import wrappers


async def select_svatek_count(name):
    url = f"Users/GetByNameCount/{name}"
    response_json = await wrappers.get_async(url)
    return response_json


async def select_narozky_count(day, month):
    url = f"Users/GetByDateCount/{day},{month}"
    response_json = await wrappers.get_async(url)
    return response_json
