# Анализ текста сайта
### Вариант 7: https://bloknot-volgograd.ru/

В данном репозитории находится сервис для обработки содержания новостного сайта. 
В `controllers/main_controller/main_controller.py` содержатся методы API, с помощью которых чат-бот выводит информацию для пользователя.

## Описание методов API
- GET `/api/v1.0/page-info?page-addr=`

  **Описание:** вывод данных о новости из базы данных
  
  **Входные данные:** ссылка на новость

  **Формат выходного json:**
  ```json
  {
  "date": "string", 
  "text": "string", 
  "title": "string"
  }
  ```
  
- GET `/api/v1.0/page-info/common-words`

  **Описание:** вывод десяти наиболее часто встречающихся слов

  **Формат выходного json:**
  ```json
  {
  "words": ["string", "string"]
  }
  ```
  
- GET `/api/v1.0/page-info/summarized`

  **Описание:** вывод аннотации для новости, с которой в данный момент идет работа. Использование сервисов сбера `https://api.aicloud.sbercloud.ru/public/v2/summarizator/predict`

  **Формат выходного json:**
  ```json
  {
  "summarized": "string"
  }
  ```
  
- GET `/api/v1.0/page-info/rewrited`

  **Описание:** вывод переписанной новости, с которой в данный момент идет работа. Использование сервисов сбера `https://api.aicloud.sbercloud.ru/public/v2/rewriter/docs`

  **Формат выходного json:**
  ```json
  {
  "rewrited": "string"
  }
  ```

- GET `/api/v1.0/page-info/vip-persons`

  **Описание:** вывод всех VIP-персон, которые были найдены в тексте. Исходные данные: `https://xn--b1ats.xn--80asehdb/feed/obshchestvo/andrey-bocharov-vozglavil-top-100-vliyatelnykh-lyudey-volgogradskoy-oblasti-7478520448.html`

  **Формат выходного json:**
  ```json
  {
  "vip_persons": ["string", "string"]
  }
  ```
  
- GET `/api/v1.0/page-info/sights`

  **Описание:** вывод всех достопримечательностей , которые были найдены в тексте. Исходные данные: `https://www.kp.ru/russia/volgograd/dostoprimechatelnosti/`

  **Формат выходного json:**
  ```json
  {
  "sights": ["string", "string"]
  }
  ```
  
- GET `/api/v1.0/page-info/?words=`

  **Описание:** вывод десяти контекстных синонимов к слову word

  **Входные данные:** слово, которое содержится в статье

  **Формат выходного json:**
  ```json
  {
  "synonyms": {
    "string": "float", 
    "string": "float"
    }
  }
  ```
  
- GET `/api/v1.0/page-info/sentiment`

  **Описание:** вывод десяти контекстных синонимов к слову word
   
    **Формат выходного json:**
    ```json
    {
    "sentiments": {
      "string": "string", 
      "string": "string"
      }
    }
    ```
