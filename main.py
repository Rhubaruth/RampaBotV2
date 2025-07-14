from loadEnv import (
    load_env,
    get_discord_token,
    load_rest_api,
)
from botLoad import bot

if __name__ == "__main__":
    load_env()

    DC_TOKEN = get_discord_token()
    load_rest_api()
    print("DOCKER DID UPDATE")
    print("BLAAAAAAA AKDFJSLFJSKLDFJKDSJFOJQWEIOJWQEIOPFJEWOIFJOEWIJFOIESJFSJDKFJSIVSONIEWPRJ 54498546518941698")
    # bot.run(DC_TOKEN)
