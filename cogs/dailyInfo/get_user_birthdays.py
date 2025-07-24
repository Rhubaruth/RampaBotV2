from datetime import date

from databaseApi import (
    select_user_by_daymonth
)


async def get_user_birthdays(date: date):
    try:
        today_birthdays = await select_user_by_daymonth(
            date.day, date.month
        )
        if "status" in today_birthdays:
            return []
        return [int(row['id']) for row in today_birthdays]
    except ValueError as e:
        print(f'[VALUE-ERROR] get_user_birthdays: {e}')
        return []
    except Exception as e:
        print(f'[ERROR] get_user_birthdays: {e}')
        return []
