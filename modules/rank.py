# rank.py
import datetime
from dateutil import parser as dateparser
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")  # Small & fast

def rank_articles(articles, user_query):
    now = datetime.datetime.now(datetime.timezone.utc)

    query_embedding = model.encode(user_query, convert_to_tensor=True)

    def score(article):
        published_at = dateparser.parse(article['publishedAt'])
        time_score = -(now - published_at).total_seconds()  # More recent is better

        text = article.get('description') or article.get('content') or article.get('title', '')
        article_embedding = model.encode(text, convert_to_tensor=True)
        relevance_score = util.cos_sim(query_embedding, article_embedding).item()

        # Weighted sum: adjust weights as needed
        final_score = (0.9 * relevance_score) + (0.1 * (1 / (1 + abs(time_score) / 3600)))  # decay time by hours
        return final_score

    return sorted(articles, key=score, reverse=True)[:10]  # Top 10
