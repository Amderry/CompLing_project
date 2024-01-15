import psycopg2

conn = psycopg2.connect(dbname='news', user='postgres', password='1912R', host='localhost')
print(conn)
cursor = conn.cursor()
title = "Тест"
ref = "Тест"
date_and_time = "Тест"
text = "Тест"
print(f"INSERT INTO news_table(title, ref, date, text) VALUES ('{title}', '{ref}', '{date_and_time}', '{text}');")
cursor.execute(f"INSERT INTO news_table(title, ref, date, text) VALUES ('{title}', '{ref}', '{date_and_time}', '{text}');")
conn.commit()
cursor.close()
conn.close()
