import psycopg2
from data.models.news import News
from data.models.sight import Sight
from data.models.vip import Vip
from services.text_editor import text_editor_service

def get_page_info(url):
    conn = psycopg2.connect(dbname='news', user='comp_ling', password='1912R', host='51.250.89.7', port=5432)
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM news_table nt WHERE nt.\"ref\" = '{url}'")
    page = [News(row[0], row[1], row[2], row[3], text_editor_service.normalize_text(row[4])) for row in cursor.fetchall()]
    conn.commit()
    cursor.close()
    conn.close()
    return page[0]


def get_vip_persons():
    conn = psycopg2.connect(dbname='news', user='comp_ling', password='1912R', host='51.250.89.7', port=5432)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vips")
    vips = [Vip(row[0], row[1]) for row in cursor.fetchall()]
    conn.commit()
    cursor.close()
    conn.close()
    return vips


def get_sights():
    conn = psycopg2.connect(dbname='news', user='comp_ling', password='1912R', host='51.250.89.7', port=5432)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM sights")
    sights = [Sight(row[0], row[1]) for row in cursor.fetchall()]
    conn.commit()
    cursor.close()
    conn.close()
    return sights

