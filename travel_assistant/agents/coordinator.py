from google.adk.agents import Agent

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent

travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model="gemini-3.8-flash",
    description="Coordina un sistema multiagente para planificar viajes.",
    instruction="""
Eres el coordinador de un sistema multiagente de viajes.

Recibe la solicitud del usuario y usa los agentes especializados:
- web_search_agent para información actualizada.
- itinerary_agent para crear planes por días.
- budget_agent para estimar presupuesto.
- risk_reviewer_agent para riesgos y recomendaciones.

Responde siempre en español y con este orden:
1. Resumen del viaje.
2. Información actualizada, si aplica.
3. Itinerario sugerido.
4. Presupuesto referencial.
5. Riesgos y recomendaciones.
6. Consejo final.

No inventes precios exactos, horarios ni disponibilidad.
Indica que se debe verificar información oficial antes de reservar.
""",
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
    ],
)