import discord
from discord.ext import commands
from discord import app_commands

from loadEnv import get_bot_prefix


def create_bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    prefix = get_bot_prefix()
    print(f"PREFIX: {prefix}")
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    # This is for the example purposes only, should only be used for debugging
    @app_commands.checks.has_role("Bot Manager")
    @bot.command(name="sync")
    async def sync(ctx: commands.Context):
        # sync to the guild where the command was used
        bot.tree.copy_global_to(guild=ctx.guild)
        await bot.tree.sync(guild=ctx.guild)

        await ctx.send(content="Success")

    @bot.event
    async def on_ready():
        # Load cogs
        await bot.load_extension("cogs.UserCalendar")
        await bot.load_extension("cogs.DailyInfo")

        # Sync commands
        await bot.tree.sync()
        print(f'Bot is online as {bot.user}')
        print("Commands have been synced")
    return bot
