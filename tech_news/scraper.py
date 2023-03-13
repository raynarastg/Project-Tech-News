# Requisito 1

import re
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
    selector = Selector(text=html_content)
    return selector.css('.next::attr(href)').get()


# def generic_get(param, value):
#     selector = Selector(text=param)
#     return selector.css(value).get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get().strip('\xa0')
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    reading_time = int(selector.css(
        '.meta-reading-time::text').get().split(' ')[0])
    sumary = selector.css('.entry-content p').get()
    sumary = re.sub('<.*?>', '', sumary).strip()
    category = selector.css('.meta-category .label::text').get()
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': sumary,
        'category': category
    }
    # return {
    #        'url': generic_get(html_content,
    #                           'link[rel="canonical"]::attr(href)'),
    #        'title': generic_get(html_content,
    #                             'h1.entry-title::text'),
    #        'timestamp': generic_get(html_content,
    #                                 '.meta-date::text'),
    #        'writer': generic_get(html_content,
    #                              'span.author a::text'),
    #        'reading_time': generic_get(html_content,
    #                                    'li.meta-reading-time::text'),
    #        'sumary': generic_get(html_content,
    #                              'div.entry-content p::text'),
    #        'category': generic_get(html_content,
    #                                'li.meta-category .label::text'),
    # }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
