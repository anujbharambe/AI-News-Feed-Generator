import datetime
from dateutil import parser as dateparser

def time_ago(published_at):
    delta = datetime.datetime.now(datetime.timezone.utc) - dateparser.parse(published_at)
    minutes = delta.total_seconds() // 60
    if minutes < 60:
        return f"{int(minutes)} minutes ago"
    hours = minutes // 60
    return f"{int(hours)} hours ago"


def display_feed(articles):
    print("\nTop Trending News Articles:\n")
    if not articles:
        print("No articles found for the given topic.")
        return
    for idx, article in enumerate(articles):
        print(f"{idx+1}. {article['title']}")
        print(f"   📝 {article['summary']}")
        print(f"   🔗 {article['url']}")
        print(f"   🕒 {time_ago(article['publishedAt'])}\n")