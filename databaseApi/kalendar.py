from databaseApi import wrappers

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
    url = f"Kalendars/GetByName/{first_name}"
    response_json = await wrappers.get_async(url=url)
    return response_json


async def select_nameday_by_daymonth(day, month):
    """
    Najde jména(nameday) podle data.
    Vrací list.
    """
    url = f"Kalendars/GetByDate/{day},{month}"
    response_json = await wrappers.get_async(url=url)
    return response_json


async def select_holiday_by_daymonth(day, month):
    """
    Najde svatek(holiday) podle data.
    Vrací list.
    """
    url = f"Kalendars/SvatekGetByDate/{day},{month}"
    response_json = await wrappers.get_async(url=url)
    return response_json


async def select_fact_by_daymonth(day, month):
    """
    Najde fakt(fact) podle data.
    Vrací list.
    """
    url = f"Kalendars/FaktGetByDate/{day},{month}"
    response_json = await wrappers.get_async(url=url)
    return response_json
