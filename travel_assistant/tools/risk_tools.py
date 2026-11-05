def assess_basic_travel_risks(destination: str, season: str) -> dict:
    """Devuelve riesgos básicos y recomendaciones para un viaje."""
    destination_normalized = destination.lower().strip()
    season_normalized = season.lower().strip()
    risks = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        risks.append(
            "Consider altitude sickness prevention and gradual acclimatization."
        )

    if "lluvia" in season_normalized or "rain" in season_normalized:
        risks.append(
            "Carry waterproof clothing and check road or trail conditions."
        )

    if "alta" in season_normalized or "high" in season_normalized:
        risks.append(
            "Book hotels, trains and entrance tickets in advance."
        )

    if not risks:
        risks.append(
            "Check weather, local transport, health requirements and travel documentation."
        )

    return {
        "status": "success",
        "destination": destination,
        "season": season,
        "risks": risks,
    }