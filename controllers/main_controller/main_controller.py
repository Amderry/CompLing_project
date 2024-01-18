from services.db import context
from services.spark import spark_service

def get_page_info(url):
    page = context.get_page_info(url)

    session = spark_service.start_session()

    filtered, sorted = spark_service.get_spark_info(session, page.text)
    print(filtered, '\n\n', sorted)
    print(get_word_synonyms(input()))
    session.stop()

def get_word_synonyms(word):
    try:
        synonyms_dict = spark_service.find_synonyms(word)
        return 200, synonyms_dict
    except Exception as ex:
        return 500, ex
get_page_info('https://bloknot-volgograd.ru/news/top-model-natalya-vodyanova-podderzhala-sladkiy-bi')