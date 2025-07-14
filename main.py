from loadEnv import get_discord_token
from botLoad import bot

if __name__ == "__main__":
    print("hello world")
    DC_TOKEN = get_discord_token()
    bot.run(DC_TOKEN)
