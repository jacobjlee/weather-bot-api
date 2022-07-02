from typing import Dict, Union

from pydantic import BaseModel


class SummaryResponseItem(BaseModel):
    greeting: str
    temperature: str
    heads_up: str


class SummaryResponse(BaseModel):
    summary: SummaryResponseItem
