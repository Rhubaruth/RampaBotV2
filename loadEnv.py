import os
from dotenv import load_dotenv

env_path = "./.env"


def get_discord_token():
    load_dotenv(env_path)
    return os.getenv('DISCORD_TOKEN')
