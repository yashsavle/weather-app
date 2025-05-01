# Weather API Wrapper

## Project Overview

This project fetches weather data from the Visual Crossing Weather API. The API  supports fetching weather data for "today" with additional parameters like `unitGroup`, `include`, and `contentType`.
Reference: [Roadmap.sh Weather API](https://roadmap.sh/projects/weather-api-wrapper-service)

## Features

- **Fetch Weather Data**: Retrieve weather data by location (city name, ZIP code, or coordinates) with an optional date
  range.
- **Caching**: Uses Redis to cache weather data for 12 hours, reducing external API calls and improving response times.
- **Rate Limiting**: Limits API requests to 100 per hour per client to prevent abuse.
- **Error Handling**: Handles cases such as invalid locations, third-party API failures, and internal server errors.

## Technologies Used

- **Flask**: Python web framework for building the API.
- **Requests**: Python library for making HTTP requests to the third-party weather API.
- **Redis**: In-memory data structure store used for caching.
- **RateLimit**: Library used for rate limiting API requests.
- **Visual Crossing Weather API**: External API used to fetch weather data.

## API Usage

### Base URL

The API is hosted locally at:  
`http://localhost:5000/weather`

### Request Format

#### Example Request

```bash
curl "http://localhost:5000/weather?location=Mumbai"
```

### Query Parameters

- `location` (required): The location for which to retrieve weather data. Can be a city name, ZIP code, or coordinates.
- `date1` (optional): The start date for which to retrieve weather data in `yyyy-MM-dd` format. If omitted, it defaults to "today".
- `date2` (optional): The end date for which to retrieve weather data in `yyyy-MM-dd` format.

### Response

The API returns weather data in JSON format, including daily and hourly details.

#### Example Response:

```json
{
  "address": "Mumbai",
  "days": [
    {
      "cloudcover": 14.6,
      "conditions": "Clear",
      "datetime": "2025-04-30",
      "datetimeEpoch": 1745951400,
      "description": "Clear conditions throughout the day.",
      "dew": 74.6,
      "feelslike": 92.1,
      "feelslikemax": 98.6,
      "feelslikemin": 88.0,
      "hours": [
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "00:00:00",
          "datetimeEpoch": 1745951400,
          "dew": 75.1,
          "feelslike": 89.3,
          "humidity": 78.91,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 15.0,
          "snow": null,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 230.0,
          "windgust": 7.4,
          "windspeed": 3.4
        },
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "01:00:00",
          "datetimeEpoch": 1745955000,
          "dew": 75.1,
          "feelslike": 89.3,
          "humidity": 78.91,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 240.0,
          "windgust": 4.5,
          "windspeed": 3.4
        },
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "02:00:00",
          "datetimeEpoch": 1745958600,
          "dew": 75.1,
          "feelslike": 89.3,
          "humidity": 78.91,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 210.0,
          "windgust": 4.0,
          "windspeed": 4.7
        },
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "03:00:00",
          "datetimeEpoch": 1745962200,
          "dew": 73.3,
          "feelslike": 88.1,
          "humidity": 74.29,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 230.0,
          "windgust": 3.4,
          "windspeed": 3.4
        },
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "04:00:00",
          "datetimeEpoch": 1745965800,
          "dew": 73.3,
          "feelslike": 88.1,
          "humidity": 74.29,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 240.0,
          "windgust": 1.8,
          "windspeed": 3.4
        },
        {
          "cloudcover": 25.0,
          "conditions": "Partially cloudy",
          "datetime": "05:00:00",
          "datetimeEpoch": 1745969400,
          "dew": 73.3,
          "feelslike": 88.1,
          "humidity": 74.29,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 0.0,
          "windgust": 1.8,
          "windspeed": 0.0
        },
        {
          "cloudcover": 50.0,
          "conditions": "Partially cloudy",
          "datetime": "06:00:00",
          "datetimeEpoch": 1745973000,
          "dew": 73.3,
          "feelslike": 88.1,
          "humidity": 74.29,
          "icon": "partly-cloudy-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1008.0,
          "severerisk": 15.0,
          "snow": null,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB"
          ],
          "temp": 82.3,
          "uvindex": 0.0,
          "visibility": 1.9,
          "winddir": 220.0,
          "windgust": 1.6,
          "windspeed": 3.4
        },
        {
          "cloudcover": 50.0,
          "conditions": "Partially cloudy",
          "datetime": "07:00:00",
          "datetimeEpoch": 1745976600,
          "dew": 76.1,
          "feelslike": 94.6,
          "humidity": 74.54,
          "icon": "partly-cloudy-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1008.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "obs",
          "stations": [
            "VABB",
            "VAJJ"
          ],
          "temp": 85.1,
          "uvindex": 0.0,
          "visibility": 2.5,
          "winddir": 86.0,
          "windgust": 1.1,
          "windspeed": 1.6
        },
        {
          "cloudcover": 50.0,
          "conditions": "Partially cloudy",
          "datetime": "08:00:00",
          "datetimeEpoch": 1745980200,
          "dew": 75.1,
          "feelslike": 93.7,
          "humidity": 72.24,
          "icon": "partly-cloudy-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1009.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.3,
          "solarradiation": 96.0,
          "source": "obs",
          "stations": [
            "VABB",
            "VAJJ"
          ],
          "temp": 85.1,
          "uvindex": 1.0,
          "visibility": 2.5,
          "winddir": 175.0,
          "windgust": 1.3,
          "windspeed": 5.2
        },
        {
          "cloudcover": 50.0,
          "conditions": "Partially cloudy",
          "datetime": "09:00:00",
          "datetimeEpoch": 1745983800,
          "dew": 76.1,
          "feelslike": 98.6,
          "humidity": 68.49,
          "icon": "partly-cloudy-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1009.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 1.1,
          "solarradiation": 313.0,
          "source": "obs",
          "stations": [
            "VABB",
            "VAJJ"
          ],
          "temp": 87.7,
          "uvindex": 3.0,
          "visibility": 2.5,
          "winddir": 187.0,
          "windgust": 2.7,
          "windspeed": 5.9
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "10:00:00",
          "datetimeEpoch": 1745987400,
          "dew": 71.1,
          "feelslike": 88.0,
          "humidity": 67.08,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1010.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 1.9,
          "solarradiation": 540.0,
          "source": "fcst",
          "stations": null,
          "temp": 83.2,
          "uvindex": 5.0,
          "visibility": 15.0,
          "winddir": 339.3,
          "windgust": 3.8,
          "windspeed": 2.5
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "11:00:00",
          "datetimeEpoch": 1745991000,
          "dew": 71.1,
          "feelslike": 89.0,
          "humidity": 65.54,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1010.0,
          "severerisk": 5.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 2.7,
          "solarradiation": 740.0,
          "source": "fcst",
          "stations": null,
          "temp": 83.9,
          "uvindex": 7.0,
          "visibility": 15.0,
          "winddir": 315.6,
          "windgust": 5.6,
          "windspeed": 4.0
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "12:00:00",
          "datetimeEpoch": 1745994600,
          "dew": 71.3,
          "feelslike": 90.2,
          "humidity": 64.07,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1009.0,
          "severerisk": 5.0,
          "snow": null,
          "snowdepth": null,
          "solarenergy": 3.2,
          "solarradiation": 888.0,
          "source": "fcst",
          "stations": null,
          "temp": 84.8,
          "uvindex": 9.0,
          "visibility": 15.0,
          "winddir": 303.3,
          "windgust": 6.3,
          "windspeed": 5.6
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "13:00:00",
          "datetimeEpoch": 1745998200,
          "dew": 72.6,
          "feelslike": 91.7,
          "humidity": 66.09,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1009.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 3.5,
          "solarradiation": 971.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.2,
          "uvindex": 10.0,
          "visibility": 15.0,
          "winddir": 288.5,
          "windgust": 9.2,
          "windspeed": 8.7
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "14:00:00",
          "datetimeEpoch": 1746001800,
          "dew": 73.3,
          "feelslike": 92.5,
          "humidity": 67.32,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1008.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 3.5,
          "solarradiation": 981.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.4,
          "uvindex": 10.0,
          "visibility": 15.0,
          "winddir": 291.6,
          "windgust": 12.3,
          "windspeed": 11.2
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "15:00:00",
          "datetimeEpoch": 1746005400,
          "dew": 74.0,
          "feelslike": 93.2,
          "humidity": 68.97,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 3.3,
          "solarradiation": 916.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.4,
          "uvindex": 9.0,
          "visibility": 15.0,
          "winddir": 297.1,
          "windgust": 14.5,
          "windspeed": 12.8
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "16:00:00",
          "datetimeEpoch": 1746009000,
          "dew": 75.3,
          "feelslike": 94.6,
          "humidity": 71.53,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 30.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 2.8,
          "solarradiation": 782.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.6,
          "uvindex": 8.0,
          "visibility": 15.0,
          "winddir": 298.3,
          "windgust": 15.9,
          "windspeed": 13.2
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "17:00:00",
          "datetimeEpoch": 1746012600,
          "dew": 76.0,
          "feelslike": 95.1,
          "humidity": 73.68,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 15.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 2.1,
          "solarradiation": 592.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.4,
          "uvindex": 6.0,
          "visibility": 15.0,
          "winddir": 290.4,
          "windgust": 14.8,
          "windspeed": 11.9
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "18:00:00",
          "datetimeEpoch": 1746016200,
          "dew": 76.7,
          "feelslike": 95.6,
          "humidity": 75.9,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 19.0,
          "snow": null,
          "snowdepth": null,
          "solarenergy": 1.3,
          "solarradiation": 367.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.2,
          "uvindex": 4.0,
          "visibility": 15.0,
          "winddir": 289.6,
          "windgust": 16.6,
          "windspeed": 13.4
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "19:00:00",
          "datetimeEpoch": 1746019800,
          "dew": 76.6,
          "feelslike": 94.5,
          "humidity": 76.77,
          "icon": "clear-day",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 38.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.5,
          "solarradiation": 141.0,
          "source": "fcst",
          "stations": null,
          "temp": 84.6,
          "uvindex": 1.0,
          "visibility": 15.0,
          "winddir": 296.9,
          "windgust": 20.8,
          "windspeed": 17.0
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "20:00:00",
          "datetimeEpoch": 1746023400,
          "dew": 77.1,
          "feelslike": 94.7,
          "humidity": 78.61,
          "icon": "clear-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1006.0,
          "severerisk": 38.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "fcst",
          "stations": null,
          "temp": 84.5,
          "uvindex": 0.0,
          "visibility": 15.0,
          "winddir": 302.2,
          "windgust": 23.0,
          "windspeed": 18.1
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "21:00:00",
          "datetimeEpoch": 1746027000,
          "dew": 76.7,
          "feelslike": 94.7,
          "humidity": 77.23,
          "icon": "clear-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1007.0,
          "severerisk": 30.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "fcst",
          "stations": null,
          "temp": 84.6,
          "uvindex": 0.0,
          "visibility": 15.0,
          "winddir": 310.0,
          "windgust": 21.3,
          "windspeed": 15.7
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "22:00:00",
          "datetimeEpoch": 1746030600,
          "dew": 76.0,
          "feelslike": 94.5,
          "humidity": 74.54,
          "icon": "clear-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1008.0,
          "severerisk": 30.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "fcst",
          "stations": null,
          "temp": 85.0,
          "uvindex": 0.0,
          "visibility": 15.0,
          "winddir": 316.1,
          "windgust": 16.3,
          "windspeed": 11.2
        },
        {
          "cloudcover": 0.0,
          "conditions": "Clear",
          "datetime": "23:00:00",
          "datetimeEpoch": 1746034200,
          "dew": 76.0,
          "feelslike": 93.9,
          "humidity": 75.4,
          "icon": "clear-night",
          "precip": 0.0,
          "precipprob": 0.0,
          "preciptype": null,
          "pressure": 1008.0,
          "severerisk": 30.0,
          "snow": 0.0,
          "snowdepth": null,
          "solarenergy": 0.0,
          "solarradiation": 0.0,
          "source": "fcst",
          "stations": null,
          "temp": 84.6,
          "uvindex": 0.0,
          "visibility": 15.0,
          "winddir": 300.5,
          "windgust": 13.4,
          "windspeed": 9.2
        }
      ],
      "humidity": 73.0,
      "icon": "clear-day",
      "moonphase": 0.08,
      "precip": 0.0,
      "precipcover": 0.0,
      "precipprob": 0.0,
      "preciptype": null,
      "pressure": 1007.5,
      "severerisk": 38.0,
      "snow": 0.0,
      "snowdepth": null,
      "solarenergy": 26.2,
      "solarradiation": 305.3,
      "source": "comb",
      "stations": [
        "VABB",
        "VAJJ"
      ],
      "sunrise": "06:11:29",
      "sunriseEpoch": 1745973689,
      "sunset": "19:00:39",
      "sunsetEpoch": 1746019839,
      "temp": 84.2,
      "tempmax": 87.7,
      "tempmin": 82.3,
      "uvindex": 10.0,
      "visibility": 9.6,
      "winddir": 289.1,
      "windgust": 23.0,
      "windspeed": 18.1
    }
  ],
  "latitude": 18.9402,
  "longitude": 72.8348,
  "queryCost": 1,
  "resolvedAddress": "Mumbai, MH, India",
  "stations": {
    "VABB": {
      "contribution": 0.0,
      "distance": 20023.0,
      "id": "VABB",
      "latitude": 19.12,
      "longitude": 72.84,
      "name": "VABB",
      "quality": 50,
      "useCount": 0
    },
    "VAJJ": {
      "contribution": 0.0,
      "distance": 19081.0,
      "id": "VAJJ",
      "latitude": 19.11,
      "longitude": 72.81,
      "name": "VAJJ",
      "quality": 21,
      "useCount": 0
    }
  },
  "timezone": "Asia/Kolkata",
  "tzoffset": 5.5
}

```

## Installation

### Prerequisites

- **Python 3.10+**
- **Redis**: Ensure that Redis is installed and running.
- **Visual Crossing Weather API Key**: Sign up and obtain an API key
  from [Visual Crossing](https://www.visualcrossing.com/).

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/alinakitieva/weather_api.git
   cd weather_api
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   Create a `.env` file and add your Visual Crossing API key:

   ```bash
   WEATHER_API_KEY=your_api_key
   ```

5. **Run Redis**:
   Make sure Redis is running locally. If Redis isn't installed, you can install it on macOS using:

   ```bash
   brew install redis
   ```

   Start Redis:

   ```bash
   redis-server
   ```

6. **Run the Flask App**:

   ```bash
   python app.py
   ```

7. **Test the API**:
   Use `curl` or a browser to access the API:

   ```bash
   curl "http://localhost:5000/weather?location=San%20Jose"
   ```

## Rate Limiting

The API limits requests to **100 requests per hour per client**. If this limit is exceeded, the API will return a
`429 Too Many Requests` response.

## Caching

Redis is used to cache weather data for **12 hours**. If a request is made for the same location and date within this
timeframe, the cached data will be returned instead of making a new API call to the external service.

## Error Handling

The API includes error handling for the following scenarios:

- **Invalid Location**: Returns an error if the location cannot be found.
- **Service Unavailable**: Returns an error if the third-party API is down.
- **Rate Limit Exceeded**: Prevents abuse by limiting the number of API requests per hour.
