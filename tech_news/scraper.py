# Requisito 1
import time
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError, ReadTimeout, HTTPError


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
