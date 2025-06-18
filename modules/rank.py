import datetime
from dateutil import parser as dateparser

def rank_articles(articles):
    def score(article):
        date_score = (datetime.datetime.now(datetime.timezone.utc) - dateparser.parse(article['publishedAt'])).total_seconds()
        return -date_score  # More recent = higher score

    return sorted(articles, key=score)[:10]  # Top 10 recent articles
