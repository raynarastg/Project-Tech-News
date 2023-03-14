import datetime

from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news_found = []
    titles = ({"title": {'$regex': title, '$options': 'i'}})
    notices = search_news(titles)
    for notice in notices:
        news_found.append((notice['title'], notice['url']))
    return news_found

# https://pt.stackoverflow.com/questions/496212/fazer-uma-consulta-com-pymongo-filtrando-por-uma-string-ignorando-letras-maiuscu


# Requisito 8
def search_by_date(date):
    try:
        news_found = []
        date_formated = datetime.datetime.fromisoformat(date).strftime(
            "%d/%m/%Y")
        dates = {'timestamp': date_formated}
        notices = search_news(dates)
        for notice in notices:
            news_found.append((notice['title'], notice['url']))
        return news_found
    except ValueError:
        raise ValueError('Data inválida')
# https://docs.python.org/3/library/datetime.html


# Requisito 9
def search_by_category(category):
    news_found = []
    titles = ({"category": {'$regex': category, '$options': 'i'}})
    notices = search_news(titles)
    for notice in notices:
        news_found.append((notice['title'], notice['url']))
    return news_found
