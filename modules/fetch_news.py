import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news_articles(user_prompt: str):
    url = f"https://newsapi.org/v2/everything?q={user_prompt}&pageSize=20&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if not data.get("articles"):
        print("API response:", data)
    articles = [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "publishedAt": article["publishedAt"],
            "content": article.get("content", "")
        }
        for article in data.get("articles", [])
    ]
    return articles
