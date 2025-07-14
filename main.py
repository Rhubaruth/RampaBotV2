from loadEnv import get_discord_token, load_rest_api
from botLoad import bot

if __name__ == "__main__":
    print("hello world")
    DC_TOKEN = get_discord_token()
    load_rest_api()
    bot.run(DC_TOKEN)
