from datetime import date

from databaseApi import (
    select_narozky_by_day_month
)


async def get_user_birthdays(date: date):
    try:
        today_birthdays = await select_narozky_by_day_month(
            date.day, date.month
        )
        if "status" in today_birthdays:
            return []
    except Exception as e:
        print(f'[ERROR] get_user_birthdays: {e}')
        return
    return [row['id'] for row in today_birthdays]
