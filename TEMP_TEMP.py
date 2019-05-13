import requests


res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "iLA6lN19IlY5kRBVTjNxnw", "isbns": "9782075094559"})

print(res.json())