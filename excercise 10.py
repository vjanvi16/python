
import requests
quary = input("What type of news are you intrested in ? ")
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-08-27&sortBy=publishedAt&apiKey=API_KEY"
r = requests.get(url)
print(r.text)