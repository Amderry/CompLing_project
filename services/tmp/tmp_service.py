import os
from data.models.news import News

def save_tmp(page):
    with open(f'{os.getcwd()}/data/data.tmp', 'w', encoding='utf-8') as file:
        file.write(f'{page.id}\n{page.title}\n{page.ref}\n{page.date}\n{page.text}')

def load_tmp():
    with open(f'{os.getcwd()}/data/data.tmp', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return News(lines[0], lines[1], lines[2], lines[3], lines[4])

