import os
from dotenv import load_dotenv

env_path = ".env"

URL_REST_API = ""
REST_API_KEY = ""

MODERATOR_ROLES = []


def load_env():
    result = load_dotenv(env_path)
    print(f"{env_path} loading result: {result}")

    # Load Roles
    try:
        admin = int(os.getenv('ADMIN_ROLE_ID'))
        developer = int(os.getenv('DEV_ROLE_ID'))
        MODERATOR_ROLES.append(admin)
        MODERATOR_ROLES.append(developer)
    except ValueError as e:
        print(f'[ERROR] loadEnv: parsing roles id ended with error [{e}].')

    # Load RestAPI
    global URL_REST_API, REST_API_KEY
    # TODO - remove the global variable

    URL_REST_API = os.getenv('URL_REST_API')
    REST_API_KEY = os.getenv('REST_API_KEY')
    return URL_REST_API, REST_API_KEY


def get_discord_token():
    return os.getenv('DISCORD_TOKEN')


def get_bot_prefix():
    return os.getenv('PREFIX')


def get_guild_id():
    return os.getenv('GUILD_ID')


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
