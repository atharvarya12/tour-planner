import requests
from config import NEWS_API_KEY

def get_news(location):
    url = f"https://newsapi.org/v2/everything?q={location}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [{"title": article["title"], "description": article["description"]} for article in articles]
