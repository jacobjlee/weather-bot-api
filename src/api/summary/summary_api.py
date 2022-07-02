from fastapi import APIRouter, Query

from schemas.summary import SummaryResponse

from api.summary.external_api import get_current_info,  get_forecast_info, get_historical_info
from api.summary.helpers import get_current_results

router = APIRouter()


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
    greeting_response = await get_current_info(lat=lat, lon=lon)
    greeting_results = get_current_results(**greeting_response)

    results = dict(greeting=greeting_results, temperature='1', heads_up='1')
    return results
