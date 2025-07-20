import datetime as dt
from timeFunctions.CentralEuropeTime import CZECH_TIMEZONE
from cogs.dailyInfo.TodayInfo import TodayInfo

from loadEnv import MODERATOR_ROLES

from discord import Client, TextChannel
from discord.ext import commands, tasks
from helperFunction import concat_list

# časy, ve kterých se daný task zapne
MIDNIGHT_TIME = dt.time(hour=0, minute=15, tzinfo=CZECH_TIMEZONE)
MORNING_TIME = dt.time(hour=6, minute=30, tzinfo=CZECH_TIMEZONE)
EVENING_TIME = dt.time(hour=20, minute=00, tzinfo=CZECH_TIMEZONE)


# Cog pro vytvoření tasků
class DailyInfoCog(commands.Cog):
    def __init__(self, bot):
        self.Info: TodayInfo = TodayInfo()

        self.main_channel: TextChannel = None
        self.bot_channel: TextChannel = None
        self.is_testbot: bool = False

        self.main_channel_id: int
        self.bot_channel_id: int

        self.bot: Client = bot

    async def cog_load(self) -> None:
        from loadEnv import get_channels
        channels = get_channels()
        main_channel_id = int(channels["general"])
        bot_channel_id = int(channels["bot"])

        self.main_channel = self.bot.get_channel(main_channel_id)
        self.bot_channel = self.bot.get_channel(bot_channel_id)

        # Do not spam while debugging
        if main_channel_id == bot_channel_id:
            self.is_testbot = True
        else:
            self.at_midnight.start()
            self.at_morning.start()
            self.at_evening.start()

        # Load today's date
        await self.at_midnight()
        await self.at_morning()

        # for Debugg
        print(self.Info.print())

    async def cog_unload(self) -> None:
        if self.is_testbot:
            return
        self.at_midnight.cancel()
        self.at_morning.cancel()
        self.at_evening.cancel()

    @tasks.loop(time=MIDNIGHT_TIME)
    async def at_midnight(self):
        datetime_now = dt.datetime.now(CZECH_TIMEZONE)
        # Debug - set specific day
        datetime_now = dt.datetime(2025, 8, 14, 18, 00, tzinfo=CZECH_TIMEZONE)
        await self.Info.set_date(datetime_now.date())

        # TODO - add Tournament Stuff
        pass

    @tasks.loop(time=MORNING_TIME)
    async def at_morning(self):

        names = concat_list(
            list(map(lambda x: f"**{x}**", self.Info.names))
        )

        message = "Cuc lidové! :meowdy:\n"
        message += f"Dnes je **{self.Info.current_date}**"
        if names:
            message += f" a svátek má {names}"
        message += ".\n"
        if self.Info.birthday_ids:
            bday_mentions = concat_list(
                list(map(lambda x: f"<@{x}>", self.Info.birthday_ids))
            )
            message += f"Všechno nejlepší k narozeninám: {bday_mentions}!\n"
        if self.Info.nameday_ids:
            nday_mentions = concat_list(
                list(map(lambda x: f"<@{x}>", self.Info.nameday_ids))
            )
            message += f"Svátek mají lidové {nday_mentions}.\n"

        print(message)
        return message

    @tasks.loop(time=EVENING_TIME)
    async def at_evening(self):
        pass

    @commands.command(name="morning")
    @commands.has_any_role(*MODERATOR_ROLES)
    async def test_morning(self, ctx: commands.Context):
        await ctx.message.delete()
        message = await self.at_morning()
        await ctx.send(message)

    @commands.command(name="print_info")
    @commands.has_any_role(*MODERATOR_ROLES)
    async def print_info(self, ctx):
        print(self.Info.print())
        await ctx.message.delete()


async def setup(bot):
    await bot.add_cog(DailyInfoCog(bot))
