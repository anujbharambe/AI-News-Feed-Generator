import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_articles(articles):
    summaries = []
    model = genai.GenerativeModel("gemini-flash-001") 
    for article in articles:
        content = article['description'] or article['content']
        if not content:
            summary = "[Summary unavailable]"
        else:
            try:
                prompt = f"Summarize this news article in 60 words:\n{content}"
                response = model.generate_content(prompt)
                summary = response.text.strip()
            except Exception as e:
                summary = "[Summary unavailable]"
        summaries.append({
            **article,
            "summary": summary
        })
    return summaries