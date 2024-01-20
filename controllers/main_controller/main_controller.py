import xml

from services.db import context
from services.spark import spark_service
from services.sber import sber_service
from services.tomita_parser import tomita_service
from flask import Flask, jsonify, abort, request
from services.tmp import tmp_service
from services.dostoevsky import dostoevsky_service

app = Flask(__name__)

@app.route('/api/v1.0/page-info', methods=['GET'])
def get_page():
    try:
        url = request.args.get('page-addr')
        page = context.get_page_info(url)
        tmp_service.save_tmp(page)
        return jsonify({'title': page.title, 'text': page.text, 'date': page.date})
    except:
        abort(404)

@app.route('/api/v1.0/page-info/common-words', methods=['GET'])
def get_common_words():
    try:
        page = tmp_service.load_tmp()
        filtered, sorted = spark_service.get_spark_info(session, page.text)
        return jsonify({'words': sorted})
    except:
        abort(500)


@app.route('/api/v1.0/page-info/summarized', methods=['GET'])
def get_summarize():
    try:
        page = tmp_service.load_tmp()
        summarized = sber_service.summarize(page.text)
        return jsonify({'summarized': summarized})
    except:
        abort(500)



@app.route('/api/v1.0/page-info/rewrited', methods=['GET'])
def get_rewrited():
    try:
        page = tmp_service.load_tmp()
        rewrited = sber_service.rewrite(page.text)
        return jsonify({'rewrited': rewrited})
    except:
        abort(500)


@app.route('/api/v1.0/page-info/vip-persons', methods=['GET'])
def get_vip_persons():
    try:
        page = tmp_service.load_tmp()
        vip_persons = tomita_service.find_vip_persons(page.text)
        return jsonify({'vip_persons': list(vip_persons)})
    except xml.etree.ElementTree.ParseError as ex:
        abort(404)
    except Exception as ex:
        abort(500)


@app.route('/api/v1.0/page-info/sights', methods=['GET'])
def get_sights():
    try:
        page = tmp_service.load_tmp()
        sights = tomita_service.find_sights(page.text)
        return jsonify({'sights': list(sights)})
    except xml.etree.ElementTree.ParseError as ex:
        abort(404)
    except Exception as ex:
        abort(500)


@app.route('/api/v1.0/page-info/', methods=['GET'])
def get_word_synonyms():
    try:
        word = request.args.get('word')
        synonyms_dict = spark_service.find_synonyms(word)
        return jsonify({'synonyms': synonyms_dict})
    except:
        abort(404)


@app.route('/api/v1.0/page-info/sentiment', methods=['GET'])
def get_sentiment():
    try:
        page = tmp_service.load_tmp()
        response = dostoevsky_service.get_sentiment(page.text)
        return jsonify({'sentiments': response})
    except:
        abort(404)

@app.route('/api/v1.0/vips-and-sights', methods=['GET'])
def get_vips_and_sights():
    return jsonify({'vips': [vip.name for vip in context.get_vip_persons()],
                    'sights': [sight.name for sight in context.get_sights()]})




if __name__ == '__main__':
    session = spark_service.start_session()
    app.config['JSON_AS_ASCII'] = False
    app.run(host="127.0.0.1", port=8080, debug=True)
    session.stop()



# get_page_info('https://bloknot-volgograd.ru/news/top-model-natalya-vodyanova-podderzhala-sladkiy-bi')