from datetime import date

from databaseApi import (
    select_nameday_by_daymonth,
    select_holiday_by_daymonth,
    select_fact_by_daymonth,
    select_beauty_today
)
from cogs.dailyInfo.get_user_birthdays import get_user_birthdays
from cogs.dailyInfo.get_user_namedays import get_user_namedays
from helperFunction import concat_list, extract_column

from typing import Union
from discord import Member, Guild


class TodayInfo:
    def __init__(self, guild: Union[Guild, None]):
        self.guild: Guild = guild
        self.current_date: date

        self.error = ""

        self.beauty_members: list[Member] = []
        self.names: list[str] = []
        self.holidays: list[str] = []
        self.facts: list[str] = []
        self.birthday_ids: list[int] = []
        self.nameday_ids: list[int] = []

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
            f"beaty: {self.beauty_members}\n" +
            "\n" +
            f"error: {self.error}\n"
        )
        return mess

    async def _get_member(self, member_id: int):
        if self.guild is None:
            print(f"[VALUE-ERROR] TodayInfo._get_member({member_id})", end=' ')
            print("- self.guild is None")
            return

        return await self.guild.fetch_member(member_id)

    async def generate_data(self, date: date):
        # get info about today from DB
        self.error = ""
        try:
            today_beauty = await select_beauty_today()
            today_names = await select_nameday_by_daymonth(
                date.day, date.month
            )
            today_holidays = await select_holiday_by_daymonth(
                date.day, date.month
            )
            today_facts = await select_fact_by_daymonth(
                date.day, date.month
            )
        except Exception as e:
            print(f'[ERROR] generate_data@TodayInfo.py: {e}')
            self.error = e
            return

        self.names = extract_column('jmeno', today_names)
        self.holidays = extract_column('svatek', today_holidays)
        self.facts = extract_column('fakt', today_facts)

        beauty_ids = extract_column('id', today_beauty)
        self.beauty_members = [
            await self._get_member(i) for i in beauty_ids
        ]

        self.birthday_ids = await get_user_birthdays(self.current_date)
        self.nameday_ids = await get_user_namedays(self.names)

    def _get_daily_message(
        self,
        write_beauty: bool = False,
        write_holidays: bool = False,
        write_birthdays: bool = False,
        write_namedays: bool = False,
        write_fact: bool = False,
    ):

        message = "Cuc lidové! <:peepoHey:1333426487381983343>\n"
        message += f"Dnes je **{self.current_date:%d.%m.}**"
        if self.holidays:
            hdays_concat = concat_list(
                list(map(lambda x: f"*{x}*", self.holidays)),
                general_sep=', ',
                last_sep=', '
            )
            message += f" ({hdays_concat})"
        if self.names:
            names_concat = concat_list(
                list(map(lambda x: f"**{x}**", self.names))
            )
            message += f" a svátek má {names_concat}"
        if self.birthday_ids and write_birthdays:
            bday_mentions = concat_list(
                list(map(lambda x: f"<@{x}>", self.birthday_ids))
            )
            message += f"\nVšechno nejlepší k narozeninám: {bday_mentions}!"
        if self.nameday_ids and write_namedays:
            nday_mentions = concat_list(
                list(map(lambda x: f"<@{x}>", self.nameday_ids))
            )
            message += f"\nSvátek mají lidové {nday_mentions}."
        if self.beauty_members and write_beauty:
            beaty_concat = concat_list(
                list(map(
                    lambda x: f"**{x.display_name}**",
                    self.beauty_members
                ))
            )
            message += f"\nDnes to sluší: {
                beaty_concat} <:peepoCute:1333426880719753310>"
        # TODO: add fact
        return message

    def get_morning_message(self):
        return self._get_daily_message(
            write_beauty=True,
            write_holidays=True,
            write_fact=True,
            write_birthdays=True,
            write_namedays=True,
        )

    def get_evening_message(self):
        return self._get_daily_message(
            # write_beauty=True,
            write_holidays=True,
            # write_fact=True,
            # write_birthdays=True,
            # write_namedays=True,
        )
        pass
