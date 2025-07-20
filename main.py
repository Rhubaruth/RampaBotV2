from loadEnv import (
    load_env,
    get_discord_token,
)
from botLoad import create_bot

bot = None

if __name__ == "__main__":
    load_env()
    bot = create_bot()

    DC_TOKEN = get_discord_token()
    bot.run(DC_TOKEN)
