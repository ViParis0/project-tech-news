# Requisito 10
from pymongo import MongoClient
from decouple import config
from collections import Counter

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def top_5_categories():
    results = db.news.find({}, {"category": 1, "_id": 0})
    categories = [result["category"] for result in list(results)]
    category_counts = Counter(categories)
    top_5 = sorted(
        category_counts.most_common(5), key=lambda x: (-x[1], x[0])
    )
    return [x[0] for x in top_5]
