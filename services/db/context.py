import psycopg2
from data.models.news import news
from services.text_editor import text_editor_service

def get_page_info(url):
    conn = psycopg2.connect(dbname='news', user='comp_ling', password='1912R', host='51.250.89.7', port=5432)
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM news_table nt WHERE nt.\"ref\" = '{url}'")
    page = [news(row[0], row[1], row[2], row[3], text_editor_service.normalize_text(row[4])) for row in cursor.fetchall()]
    conn.commit()
    cursor.close()
    conn.close()
    return page[0]
