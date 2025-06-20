import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_articles(articles):
    summaries = []
    model = genai.GenerativeModel("gemini-2.0-flash-001") 

    for article in articles:
        content = article.get('description') or article.get('content') or ""
        image_url = article.get("top_image") or article.get("image") or "https://via.placeholder.com/150"

        if not content.strip():
            summary = "[Summary unavailable]"
        else:
            try:
                prompt = f"Summarize the following news article in under 60 words:\n\n{content[:4000]}"
                response = model.generate_content(prompt)
                summary = response.text.strip()
            except Exception as e:
                summary = "[Summary unavailable]"
        
        summaries.append({
            **article,
            "summary": summary,
            "image": image_url
        })

    return summaries
# This function uses Google's Gemini model to summarize articles.                                           
