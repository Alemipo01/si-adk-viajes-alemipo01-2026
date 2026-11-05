from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-3.8-flash",
    description="Estima presupuestos referenciales de viaje.",
    instruction="""
Eres un asesor de presupuesto de viajes.

Usa la herramienta disponible si el usuario indica destino,
cantidad de días y presupuesto diario. Explica que los montos
son referenciales y que debe verificar precios actuales.
""",
    tools=[estimate_trip_budget],
)