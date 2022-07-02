from httpx import AsyncClient, Response

from config import settings


async def get_current_info(lat: float, lon: float):
    async with AsyncClient() as client:
        params: dict = dict(lat=lat, lon=lon, api_key=settings.EXTERNAL_WEATHER_API_KEY)
        resp: Response = await client.get(settings.EXTERNAL_WEATHER_CURRENT_URL, params=params)
        return resp.json()


async def get_forecast_info(lat: float, lon: float, hour_offset: int):
    async with AsyncClient() as client:
        params: dict = dict(lat=lat, lon=lon, hour_offset=hour_offset, api_key=settings.EXTERNAL_WEATHER_API_KEY)
        resp: Response = await client.get(settings.EXTERNAL_WEATHER_FORECAST_URL, params=params)
        return resp.json()


async def get_historical_info(lat: float, lon: float, hour_offset: int):
    async with AsyncClient() as client:
        params: dict = dict(lat=lat, lon=lon, hour_offset=hour_offset, api_key=settings.EXTERNAL_WEATHER_API_KEY)
        resp: Response = await client.get(settings.EXTERNAL_WEATHER_HISTORICAL_URL, params=params)
        return resp.json()
