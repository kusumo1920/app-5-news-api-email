import requests
from dotenv import load_dotenv
import os
from send_email import send_email

load_dotenv()
topic = "tesla"

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}" \
      f"&from=2023-03-15" \
      f"&sortBy=publishedAt" \
      f"&language=en" \
      f"&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = f"Subject: News of Today\n\n"
for index, article in enumerate(content["articles"][:20]):
      body = body + str(article["title"]) \
             + "\n" + str(article["description"]) \
             + "\n" + str(article["url"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
