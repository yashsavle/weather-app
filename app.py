from flask import Flask, request, jsonify
from weather_service import fetch_weather, WeatherServiceError
from ratelimit import limits
import requests
from config import Config
from logging_config import setup_logging

app = Flask(__name__)
logger = setup_logging(Config.LOG_LEVEL, Config.LOG_FILE)

# Rate limiting: 100 requests per hour
HOUR = 3600

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@limits(calls=Config.RATE_LIMIT, period=HOUR)
@app.route("/weather", methods=["GET"])
def get_weather():
    location = request.args.get("location")
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")

    if not location:
        logger.warning("Location is missing from request")
        return jsonify({"error": "Location is required"}), 400

    try:
        weather_data = fetch_weather(location, date1, date2)
        return jsonify(weather_data)
    except WeatherServiceError as e:
        logger.error(f"Weather service error: {str(e)}")
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        logger.error(f"Internal server error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    logger.debug(f"Unhandled request to: {path}")
    return jsonify({"error": "Invalid endpoint"}), 404


if __name__ == "__main__":
    app.run(debug=True)
