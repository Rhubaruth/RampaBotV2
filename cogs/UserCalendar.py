from discord import Interaction
from discord.ext import commands
from discord import app_commands

from cogs.userCalendar import jmeniny
from cogs.userCalendar.jmeniny import JmeninyError
from cogs.userCalendar import narozeniny
from cogs.userCalendar.narozeniny import NarozeninyError

from datetime import date


class UserCalendarCog(commands.Cog):
    """
    Cog for user commands that interacts with calendar.

    /narozeniny <datum>
    /svatek <jmeno>
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="narozeniny",
        description="Nastavení data narozenin uživatele."
    )
    async def narozeniny(
            self, interaction: Interaction,
            day: int, month: int,
    ):
        user = interaction.user
        try:
            bdate = date(year=2024, month=month, day=day)
        except ValueError as e:
            await interaction.response.send_message(
                f"Chyba - Neexistující datum **{day}.{month}.**.\n[{e}]",
                ephemeral=True
            )
            return

        try:
            result, arg = await narozeniny.set_narozeniny(user, bdate)
        except Exception as e:
            print(f"[ERROR] narozeniny@UserCalendar.py: {e}")
            return
        await interaction.response.send_message(
            f"result: {result} | arg: {arg}",
            ephemeral=True
        )

    @app_commands.command(
        name="svatek",
        description="Nastavení svátku uživatele."
    )
    async def jmeniny(
        self,
        interaction: Interaction,
        name: str,
    ):
        user = interaction.user
        try:
            result, arg = await jmeniny.set_jmeniny(user, name)
        except Exception as e:
            result = None
            await interaction.response.send_message(
                f"Chyba při komunikaci s API. ({e})",
                ephemeral=True
            )
            # TODO - send PM to @Rhubaruth
            print("[Error] jmeniny@UserCalendar.py: ", {e})
            return
        message = ""
        if result is JmeninyError.OK and arg is None:
            message = f"Jméno {user.mention} bylo nastaveno na **{name}**."
        elif result is JmeninyError.OK:
            message = f"Jméno {user.mention} bylo změněno z {
                arg} na **{name}**."
        elif result is JmeninyError.AlreadySet:
            message = f"Jméno {user.mention} už je nastaveno na **{arg}**."
        elif result is JmeninyError.NameNotFound:
            message = f"Jméno **{name}** nebylo nalezeno v databázi."
        else:
            message = f"Nastala chyba [JmeninyError.{result}]"
            # TODO - send PM to @Rhubaruth
            print("[Error] jmeniny@UserCalendar.py: ", {arg})
        await interaction.response.send_message(
            message,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(UserCalendarCog(bot))
