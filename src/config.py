from pydantic import BaseSettings


class Settings(BaseSettings):
    EXTERNAL_WEATHER_BASE_URL: str = "https://thirdparty-weather-api-v2.droom.workers.dev"
    EXTERNAL_WEATHER_CURRENT_URL: str = EXTERNAL_WEATHER_BASE_URL + "/current"
    EXTERNAL_WEATHER_FORECAST_URL: str = EXTERNAL_WEATHER_BASE_URL + "/forecast/hourly"
    EXTERNAL_WEATHER_HISTORICAL_URL: str = EXTERNAL_WEATHER_BASE_URL + "/historical/hourly"
    EXTERNAL_WEATHER_API_KEY: str = "fake_api_key"


settings = Settings()
