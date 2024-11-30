import json

# Load API keys and configurations from config.json
with open("data/config.json") as f:
    config = json.load(f)

OPENAI_API_KEY = config["openai_api_key"]
GOOGLE_MAPS_API_KEY = config["google_maps_api_key"]
OPENWEATHER_API_KEY = config["openweather_api_key"]
NEWS_API_KEY = config["news_api_key"]
NEO4J_URI = config["neo4j_uri"]
NEO4J_USER = config["neo4j_user"]
NEO4J_PASSWORD = config["neo4j_password"]
