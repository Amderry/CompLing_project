import psycopg2

conn = psycopg2.connect(dbname='news', user='postgres', password='1234', host='localhost')
print(conn)
cursor = conn.cursor()
title = "Тест"
ref = "Тест"
date_and_time = "2023-12-16"
text = "Тест"
print(f"INSERT INTO news_table(title, ref, date, text) VALUES ('{title}', '{ref}', '{date_and_time}', '{text}');")
cursor.execute(f"INSERT INTO news_table(title, ref, date, text) VALUES ('{title}', '{ref}', '{date_and_time}', '{text}');")
conn.commit()
cursor.close()
conn.close()
