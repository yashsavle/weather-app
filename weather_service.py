import requests
import json
from cache import get_cached_data, set_cached_data
from config import Config
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class WeatherServiceError(Exception):
    pass

def construct_url(location: str, date1: Optional[str] = None, date2: Optional[str] = None) -> str:
    if date1 and date2:
        return f"{Config.BASE_URL}{location}/{date1}/{date2}"
    elif date1:
        return f"{Config.BASE_URL}{location}/{date1}"
    return f"{Config.BASE_URL}{location}/today"

def fetch_weather(location: str, date1: Optional[str] = None, date2: Optional[str] = None) -> Dict:
    params = {
        "key": Config.API_KEY,
        "unitGroup": "us",
        "include": "days,hours",
        "contentType": "json",
    }
    url = construct_url(location, date1, date2)
    logger.info(f"Fetching weather data for URL: {url} with params: {params}")

    cached_data = get_cached_data(url)
    if cached_data:
        logger.info(f"Returning cached weather data for {location}")
        return json.loads(cached_data)

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        set_cached_data(url, json.dumps(weather_data), Config.CACHE_EXPIRATION)
        logger.info(f"Fetched and cached weather data for {location}")
        return weather_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        raise WeatherServiceError("Failed to fetch weather data") from e
