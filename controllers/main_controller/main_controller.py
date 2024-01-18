from services.db import context
def get_page_info(url):
    page = context.get_page_info(url)
    print(page)

get_page_info('https://bloknot-volgograd.ru/news/kotovo-ostalsya-bez-vody-posle-dorogostoyashchego--1676766')