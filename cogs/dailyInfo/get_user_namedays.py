from databaseApi import (
    select_user_by_name,
)


async def get_user_namedays(names: list[str]):
    try:
        today_namedays = []
        for name in names:
            db_result = await select_user_by_name(name)
            if "status" in db_result:
                continue
            today_namedays += db_result
        pass
    except Exception as e:
        print(f'[ERROR] get_user_namedays.py: {e}')
        return
    return [row['id'] for row in today_namedays]
