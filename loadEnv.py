import os
from dotenv import load_dotenv

env_path = ".env"

URL_REST_API = ""
REST_API_KEY = ""


def load_env():
    result = load_dotenv(env_path)
    print(f"{env_path} loading result: {result}")


def get_discord_token():
    return os.getenv('DISCORD_TOKEN')


def get_bot_prefix():
    return os.getenv('PREFIX')


def get_channels():
    return {
        "general": os.getenv('MAIN_CHANNEL'),
        "bot": os.getenv('BOT_CHANNEL'),
    }


def get_roles():
    return {
        "admin": os.getenv('ADMIN_ROLE_ID'),
        "dev": os.getenv('DEV_ROLE_ID'),
    }


def load_rest_api():
    global URL_REST_API, REST_API_KEY
    # TODO - remove the global variable

    URL_REST_API = os.getenv('URL_REST_API')
    REST_API_KEY = os.getenv('REST_API_KEY')
    return URL_REST_API, REST_API_KEY
