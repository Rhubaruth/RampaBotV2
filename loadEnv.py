import os
from dotenv import load_dotenv

env_path = "./.env"

URL_REST_API = ""
REST_API_KEY = ""


def load_rest_api():
    global URL_REST_API, REST_API_KEY

    load_dotenv(env_path)
    URL_REST_API = os.getenv('URL_REST_API')
    REST_API_KEY = os.getenv('REST_API_KEY')
    return URL_REST_API, REST_API_KEY


def get_discord_token():
    load_dotenv(env_path)
    return os.getenv('DISCORD_TOKEN')
