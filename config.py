import os
import logging
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    API_KEY = os.getenv("WEATHER_API_KEY")
    BASE_URL = os.getenv("BASE_URL", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    CACHE_EXPIRATION = int(os.getenv("CACHE_EXPIRATION", 43200))
    RATE_LIMIT = int(os.getenv("RATE_LIMIT", 100))
    LOG_LEVEL = logging.DEBUG if os.getenv("FLASK_ENV") == "development" else logging.INFO
    LOG_FILE = os.getenv("LOG_FILE", "app.log")

    @staticmethod
    def validate():
        if not Config.API_KEY:
            raise ValueError("WEATHER_API_KEY is not set in the environment variables")

Config.validate()
