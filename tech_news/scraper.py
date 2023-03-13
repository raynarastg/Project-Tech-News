# Requisito 1

import time

import requests
from parsel import Selector


# params = (url, headers, timeout)
def fetch(url):
    try:
        response = requests.get(url,
                                {"user-agent": "Fake user-agent"},
                                3)
        response
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css('.cs-overlay-link::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
