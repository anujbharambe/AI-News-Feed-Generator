from modules.fetch_news import fetch_news_articles
from modules.summarize import summarize_articles
from modules.rank import rank_articles
from modules.display import display_feed

def generate_news_feed(user_prompt: str):

    print("Fetching news articles...")
    articles = fetch_news_articles(user_prompt)
    summarized = summarize_articles(articles)
    ranked = rank_articles(summarized)
    display_feed(ranked)

if __name__ == "__main__":
    user_prompt = input("Enter a topic to get trending news: ")
    generate_news_feed(user_prompt)
