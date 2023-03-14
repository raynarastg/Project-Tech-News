# Requisito 1

import re
import time

import requests
from parsel import Selector

from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    return selector.css('.next::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get().strip('\xa0')
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    reading_time = int(selector.css(
        '.meta-reading-time::text').get().split(' ')[0])
    summary = selector.css('.entry-content p').get()
    summary = re.sub('<.*?>', '', summary).strip()
    category = selector.css('.meta-category .label::text').get()
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': summary,
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    news = []
    url = 'https://blog.betrybe.com/'
    while len(news) < amount:
        response = fetch(url)
        updates = scrape_updates(response)
        news.extend(updates)
        url = scrape_next_page_link(response)
    arr_news = []
    for i in news[:amount]:
        arr_news.append(scrape_news(fetch(i)))
    create_news(arr_news)
    return arr_news[:amount]

# fontes acessadas:
# https://www.freecodecamp.org/portuguese/news/tutorial-de-lacos-while-em-python-exemplos-de-sintaxe-while-true-e-lacos-infinitos/
# https://www.w3schools.com/python/ref_list_extend.asp
