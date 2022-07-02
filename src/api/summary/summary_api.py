import json

from fastapi import APIRouter, Query

from api.summary.external_api import get_current_info, get_forecast_info, get_historical_info
from api.summary.helpers import get_greeting_results, get_temperature_results
from schemas.summary import SummaryResponse


router = APIRouter()

HISTORICAL_HOURS = [-6, -12, -18, -24]


@router.get("/summary", response_model=SummaryResponse, tags=['summary'])
async def summary(
    lat: float = Query(
        ge=-90,
        le=90,
        description="Latitude should be greater than or equal to -90 and less than or equal to 90.",
    ),
    lon: float = Query(
        ge=-180,
        le=180,
        description="Longitude should be greater than or equal to -180 and less than or equal to 180.",
    )
):
    greeting_response: json = await get_current_info(lat=lat, lon=lon)
    greeting_results: str = get_greeting_results(**greeting_response)

    current_temp: int = int(greeting_response['temp'])
    total_temp_list: list = []
    for hour in HISTORICAL_HOURS:
        resp: json = await get_historical_info(lat=lat, lon=lon, hour_offset=hour)
        total_temp_list.append(resp['temp'])

    temperature_results: str = get_temperature_results(
        current_temp=current_temp,
        temp_24_hours_ago=int(total_temp_list[-1]),
        max_temp=int(max(total_temp_list)),
        min_temp=int(min(total_temp_list)),
    )

    results = dict(summary=dict(greeting=greeting_results, temperature=temperature_results, heads_up='1'))
    return results
