# Requisito 1
import time
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError, ReadTimeout, HTTPError

from tech_news.database import create_news


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except (ConnectionError, ReadTimeout, HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("a", class_="cs-overlay-link")
    return [str(i["href"]) for i in links if i]


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        next = soup.find("a", class_="next")
        return next["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    url = soup.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", class_="entry-title").text.rstrip()
    date = soup.find("li", class_="meta-date").text
    author = soup.find("a", class_="url fn n").text
    reading_time = soup.find("li", class_="meta-reading-time").text.split(" ")[
        0
    ]
    sumary = soup.find("div", class_="entry-content").p.text.rstrip()
    category = soup.find("span", class_="label").text
    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": author,
        "reading_time": int(reading_time),
        "summary": sumary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    blog_html = fetch("https://blog.betrybe.com/")
    news_list = []

    while len(news_list) != amount:
        next = scrape_next_page_link(blog_html)
        link_list = scrape_updates(blog_html)
        for link in link_list[:amount]:
            new = fetch(link)
            result = scrape_news(new)
            if len(news_list) == amount:
                break
            news_list.append(result)

        blog_html = fetch(next)

    create_news(news_list)
    return news_list
