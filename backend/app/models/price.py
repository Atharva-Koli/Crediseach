from pydantic import BaseModel
from typing import List


class PriceItem(BaseModel):
    source: str
    title: str
    price: float
    currency: str
    url: str


class SearchResponse(BaseModel):
    query: str
    country: str
    results: List[PriceItem]
