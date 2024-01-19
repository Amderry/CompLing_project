import os
from data.models.news import News

def save_tmp(page, filename):
    with open(f'{os.getcwd()}/data/{filename}.tmp', 'w', encoding='utf-8') as file:
        file.write(f'{page.id}\n{page.title}\n{page.ref}\n{page.date}\n{page.text}')

def load_tmp(filename):
    with open(f'{os.getcwd()}/data/{filename}.tmp', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return News(lines[0], lines[1], lines[2], lines[3], lines[4])



