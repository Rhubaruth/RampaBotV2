from discord import Interaction
from discord.ext import commands
from discord import app_commands

from userCalendar import jmeniny
from userCalendar.jmeniny import JmeninyError


class UserCalendarCog(commands.Cog):
    """
    Cog for user commands that interacts with calendar.

    /narozeniny <datum>
    /svatek <jmeno>
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="svatek",
        description="Nastavení svátku uživatele"
    )
    async def jmeniny(self, interaction: Interaction, name: str):
        user = interaction.user
        try:
            result, arg = jmeniny.set_jmeniny(user, name)
        except Exception as e:
            result = None
            # TODO - send PM to @Rhubaruth
            await interaction.response.send_message(
                "Chyba při komunikaci s API.",
                ephemeral=False
            )
            print("Error - jmeniny@UserCalendar.py:")
            print(e)
            return
        message = ""
        if result is JmeninyError.OK:
            message = f"Jméno {user.mention} bylo nastaveno na **{name}**."
        elif result is JmeninyError.AlreadySet:
            message = f"Jméno {user.mention} už je nastaveno na **{arg}**."
        elif result is JmeninyError.NameNotFound:
            message = f"Jméno **{name}** nebylo nalezeno v databázi."
        else:
            message = f"Nastala chyba [JmeninyError.{result}]"
            # TODO - send PM to @Rhubaruth
        await interaction.response.send_message(
            message,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(UserCalendarCog(bot))
