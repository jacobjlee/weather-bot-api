from fastapi import APIRouter, Query


router = APIRouter()


@router.get("/summary", tags=['summary'])
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
    items = {"lat": lat, "lon": lon}
    return items
