import json
import random

import pytest
from httpx import AsyncClient

from api import get_current_info,  get_forecast_info, get_historical_info

MIN_LAT: float = -90
MAX_LAT: float = 90
MIN_LON: float = -180
MAX_LON: float = 180
HISTORICAL_HOUR_OFFSET_LIST: list = [-6, -12, -18, -24]
FORECAST_HOUR_OFFSET_LIST: list = [6, 12, 18, 24, 30, 36, 42, 48]


@pytest.mark.asyncio
async def test_current_api():
    """Test current api request function."""
    async with AsyncClient() as client:
        params: dict = dict(lat=random.uniform(MIN_LAT, MAX_LAT), lon=random.uniform(MIN_LON, MAX_LON))
        resp: json = await get_current_info(**params)
        assert set(resp.keys()) == {"timestamp", "code", "temp", "rain1h"}


@pytest.mark.asyncio
async def test_historical_api():
    """Test historical api request function."""
    async with AsyncClient() as client:
        params: dict = dict(lat=random.uniform(MIN_LAT, MAX_LAT), lon=random.uniform(MIN_LON, MAX_LON),
                            hour_offset=random.choice(HISTORICAL_HOUR_OFFSET_LIST))
        resp: json = await get_historical_info(**params)
        assert set(resp.keys()) == {"timestamp", "code", "temp", "rain1h"}


@pytest.mark.asyncio
async def test_forecast_api():
    """Test forecast api request function."""
    async with AsyncClient() as client:
        params: dict = dict(lat=random.uniform(MIN_LAT, MAX_LAT), lon=random.uniform(MIN_LON, MAX_LON),
                            hour_offset=random.choice(FORECAST_HOUR_OFFSET_LIST))
        resp: json = await get_forecast_info(**params)
        assert set(resp.keys()) == {"timestamp", "code", "min_temp", "max_temp", "rain"}
