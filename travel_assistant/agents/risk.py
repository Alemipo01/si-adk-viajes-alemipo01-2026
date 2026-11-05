from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-3.8-flash",
    description="Revisa riesgos y recomendaciones de viaje.",
    instruction="""
Eres un revisor de riesgos de viaje.

Evalúa clima, altura, temporada, seguridad, transporte,
documentación y salud. Da recomendaciones prácticas sin alarmar.

Usa la herramienta disponible cuando el destino y temporada
estén presentes.
""",
    tools=[assess_basic_travel_risks],
)