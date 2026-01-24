from typing import List
from app.models.price import PriceItem


def normalize_serpapi_results(data: dict, limit: int = 5) -> List[PriceItem]:
    """
    Converts raw SerpAPI Google Shopping response into PriceItem objects.
    """
    results: List[PriceItem] = []

    shopping_results = data.get("shopping_results", [])

    for item in shopping_results:
        try:
            title = item.get("title")
            link = item.get("product_link")

            # Prefer numeric price if available
            price = item.get("extracted_price")

            # Fallback: parse price string
            if price is None:
                price_raw = item.get("price")
                if price_raw:
                    price = float(
                        price_raw.replace("₹", "")
                        .replace(",", "")
                        .strip()
                    )

            if not title or not price or not link:
                continue

            results.append(
                PriceItem(
                    source="google_shopping",
                    title=title,
                    price=float(price),
                    currency="INR",
                    url=link,
                )
            )

            if len(results) >= limit:
                break

        except Exception:
            continue

    return results
