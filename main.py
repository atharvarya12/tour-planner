from fastapi import FastAPI
from agents.user_interaction_agent import UserInteractionAgent
from agents.itinerary_generation_agent import ItineraryGenerationAgent
from agents.weather_agent import WeatherAgent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Tour Planner API"}

@app.post("/get_user_preferences/")
def get_user_preferences(message: str):
    response = UserInteractionAgent.get_user_preferences(message)
    return {"response": response}

@app.get("/get_weather/")
def get_weather(lat: float, lon: float):
    return {"weather": WeatherAgent.get_weather((lat, lon))}
