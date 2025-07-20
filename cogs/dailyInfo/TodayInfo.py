from datetime import date

from databaseApi import (
    select_date_by_day_month_jmeno,
    select_date_by_day_month_svatek,
    select_date_by_day_month_fakt,
    # select_user_by_name,
    # select_narozky_by_day_month,
)
from cogs.dailyInfo.get_user_birthdays import get_user_birthdays
from cogs.dailyInfo.get_user_namedays import get_user_namedays


class TodayInfo:
    def __init__(self):
        self.current_date: date

        self.error = ""

        self.names: list[str] = []
        self.holidays: list[str] = []
        self.facts: list[str] = []
        self.birthday_ids: list[str] = []
        self.nameday_ids: list[str] = []

    async def set_date(self, new_date: date):
        self.current_date = new_date
        await self.generate_data(new_date)

    def print(self) -> str:
        mess = (
            "  === TodayInfo ===\n" +
            f"date: {self.current_date}\n" +
            f"names: {self.names}\n" +
            f"holidays: {self.holidays}\n" +
            f"facts: {self.facts}\n" +
            "\n" +
            f"birthdays: {self.birthday_ids}\n" +
            f"namedays: {self.nameday_ids}\n" +
            "\n" +
            f"error: {self.error}\n"
        )
        return mess

    async def generate_data(self, date: date):
        # get info about today from DB
        self.error = ""
        try:
            today_names = await select_date_by_day_month_jmeno(
                date.day, date.month
            )
            today_holidays = await select_date_by_day_month_svatek(
                date.day, date.month
            )
            today_facts = await select_date_by_day_month_fakt(
                date.day, date.month
            )
        except Exception as e:
            print(f'[ERROR] generate_data@TodayInfo.py: {e}')
            self.error = e
            return

        self.names = [row["jmeno"] for row in today_names]
        self.holidays = [row["svatek"] for row in today_holidays]
        self.facts = [row["fakt"] for row in today_facts]

        self.birthday_ids = await get_user_birthdays(self.current_date)
        self.nameday_ids = await get_user_namedays(self.names)
