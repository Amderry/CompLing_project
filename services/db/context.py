import psycopg2
from data.models.news import news

def get_page_info(url):
    conn = psycopg2.connect(dbname='news', user='postgres', password='1234', host='localhost')
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM news_table nt WHERE nt.\"ref\" = '{url}'")
    page = [news(row[0], row[1], row[2], row[3], row[4]) for row in cursor.fetchall()]
    conn.commit()
    cursor.close()
    conn.close()
    return page[0]