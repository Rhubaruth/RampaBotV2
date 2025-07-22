import datetime as dt
from timeFunctions.CentralEuropeTime import CZECH_TIMEZONE
from cogs.dailyInfo.TodayInfo import TodayInfo

from loadEnv import MODERATOR_ROLES

from discord import Client, TextChannel
from discord.ext import commands, tasks

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
        await self.Info.set_date(datetime_now.date())

    @tasks.loop(time=MORNING_TIME)
    async def at_morning(self):
        message = self.Info.get_morning_message()

        if len(message) > 1:
            await self.main_channel.send(message)
        return message

    @tasks.loop(time=EVENING_TIME)
    async def at_evening(self):
        message = self.Info.get_evening_message()

        if len(message) > 1:
            await self.main_channel.send(message)
        return message

    @commands.command(name="morning")
    @commands.has_any_role(*MODERATOR_ROLES)
    async def test_morning(self, ctx: commands.Context):
        await ctx.message.delete()
        message = await self.at_morning()
        print(message)
        # await ctx.send(message)

    @commands.command(name="evening")
    @commands.has_any_role(*MODERATOR_ROLES)
    async def test_evening(self, ctx: commands.Context):
        await ctx.message.delete()
        message = await self.at_evening()
        print(message)
        # await ctx.send(message)

    @commands.command(name="print_info")
    @commands.has_any_role(*MODERATOR_ROLES)
    async def print_info(self, ctx):
        print(self.Info.print())
        await ctx.message.delete()


async def setup(bot):
    await bot.add_cog(DailyInfoCog(bot))
