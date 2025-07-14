import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


# This is for the example purposes only and should only be used for debugging
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
    # await bot.load_extension("cogs.<filename>")

    # Sync commands
    await bot.tree.sync()
    print(f'Bot is online as {bot.user}')
    print("Commands have been synced")
