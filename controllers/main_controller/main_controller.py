from services.db import context
from services.spark import spark_service
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app.route('/api/v1.0/page-info', methods=['GET'])
def get_page_info():
    url = request.args.get('page-addr')
    page = context.get_page_info(url)
    filtered, sorted = spark_service.get_spark_info(session, page.text)
    print(filtered, '\n\n', sorted)
    #print(get_word_synonyms(input()))
    return jsonify({'filtered': filtered, 'most_common': sorted})

@app.route('/api/v1.0/page-info/', methods=['GET'])
def get_word_synonyms():
    word = request.args.get('word')
    synonyms_dict = spark_service.find_synonyms(word)
    return jsonify({'synonyms': synonyms_dict})

@app.route('/api/v1.0/test', methods=['GET'])
def test_api():
    return jsonify('hello')

if __name__ == '__main__':
    session = spark_service.start_session()
    app.config['JSON_AS_ASCII'] = False
    app.run(host="25.51.113.175", debug=True)
    session.stop()


# get_page_info('https://bloknot-volgograd.ru/news/top-model-natalya-vodyanova-podderzhala-sladkiy-bi')