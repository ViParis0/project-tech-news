# Requisito 7
from tech_news.database import search_news


def search_by_title(title: str):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(x["title"], x["url"]) for x in result if x]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
