from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-3.8-flash",
    description="Busca información actualizada para viajes.",
    instruction="""
Eres un agente de investigación de viajes.

Busca información actualizada cuando el usuario la necesite:
atracciones, clima, restricciones, horarios y recomendaciones oficiales.

Usa Google Search. Resume de forma clara y avisa que precios
y horarios deben verificarse antes de realizar una reserva.
""",
    tools=[google_search],
)