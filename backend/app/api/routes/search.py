from fastapi import APIRouter, Query
from app.models.price import SearchResponse, PriceItem

router = APIRouter(prefix="/search", tags=["search"])


@router.get("", response_model=SearchResponse)
def search_prices(
    q: str = Query(..., description="Product name"),
    country: str = Query("IN", description="Country code"),
    limit: int = Query(5, ge=1, le=20)
):
    mock_results = [
        PriceItem(
            source="amazon",
            title=f"{q} (Sample Product)",
            price=79999,
            currency="INR",
            url="https://example.com/product"
        )
    ]

    return SearchResponse(
        query=q,
        country=country,
        results=mock_results[:limit]
    )
