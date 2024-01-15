import requests
from bs4 import BeautifulSoup
from urllib3 import Timeout
import get_proxies
import psycopg2

page = 235
counter = 0
url = "https://bloknot-volgograd.ru/?PAGEN_1="

def fetch_data(url, proxies, counter, page):
    url += str(page)
    response = requests.get(url, proxies={"https": proxies[counter]}, headers={"Accept-Language" : "en-US,en;q=0.5", "User-Agent": "Defined",}, timeout=2).text

    data = BeautifulSoup(response, 'html.parser')
    articles = data.find_all('img', class_='preview_picture')[:10]
    if page != 1:
        articles.pop(0)
    if len(data):
        for article in articles:
            for i in range(30):
                title = article['title']
                ref = 'https://bloknot-volgograd.ru' + article.find_previous()['href']
                try:
                    article_response = requests.get(ref, proxies={"https": proxies[counter]}, timeout=2).text
                    article_data = BeautifulSoup(article_response, 'html.parser')
                    newlines_text = article_data.find('div', class_='news-text').text
                    date_and_time = article_data.find('span', class_='news-date-time').text
                    text = "\n".join([ll.rstrip() for ll in newlines_text.splitlines() if ll.strip()])
                    print(title, ref, date_and_time, text, sep='\n')
                    conn = psycopg2.connect(dbname='news', user='postgres', password='1912R', host='localhost')
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO news_table(title, ref, date, text) VALUES ('{title}', '{ref}', '{date_and_time}', '{text}')")
                    conn.commit()
                    cursor.close()
                    conn.close()
                except Exception as e:
                    print(e)
                else:
                    break
                finally:
                    counter += 1
                    counter %= len(proxies)
                if i % 4 == 0:
                    get_proxies.get_proxy_list()
                    with open("proxy_list.txt", "r") as f:
                        proxies = f.read().split("\n")
        return 1
    else:
        return 0
        

while True:
    get_proxies.get_proxy_list()
    with open("proxy_list.txt", "r") as f:
        proxies = f.read().split("\n")
    for i in range(30):
        try:
            print("page is: ", page)
            if fetch_data(url, proxies, counter, page) == 0:
                quit()
            page += 1
            break
        except Exception as e:
            print(e)
        finally:
            counter += 1
            counter %= len(proxies)
        if i % 4 == 0:
            get_proxies.get_proxy_list()
            with open("proxy_list.txt", "r") as f:
                proxies = f.read().split("\n")


