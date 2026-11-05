def estimate_trip_budget(destination: str, days: int, daily_budget_usd: float) -> dict:
    """Calcula un presupuesto referencial para un viaje."""
    if days <= 0:
        return {
            "status": "error",
            "message": "The number of days must be greater than zero.",
        }

    if daily_budget_usd <= 0:
        return {
            "status": "error",
            "message": "The daily budget must be greater than zero.",
        }

    return {
        "status": "success",
        "destination": destination,
        "days": days,
        "daily_budget_usd": daily_budget_usd,
        "estimated_total_usd": days * daily_budget_usd,
    }