# modules/scrape_news.py
from newspaper import Article
import feedparser
import datetime

def scrape_google_news_articles(user_prompt):
    rss_url = f"https://news.google.com/rss/search?q={user_prompt.replace(' ', '+')}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries[:20]:
        try:
            a = Article(entry.link)
            a.download()
            a.parse()
            top_image = a.top_image
            if not top_image:
                top_image = "https://via.placeholder.com/150"  # Fallback image
            articles.append({
                "title": a.title,
                "description": entry.get("summary", ""),
                "url": entry.link,
                "publishedAt": entry.get("published", datetime.datetime.now().isoformat()),
                "content": a.text,
                "source": "GoogleNewsRSS",
                "image": top_image, 
            })
        except Exception as e:
            print(f"Failed to parse article: {entry.link}", e)

    return articles
