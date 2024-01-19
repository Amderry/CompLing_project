from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import IDF
from pyspark.ml.feature import Word2Vec, Word2VecModel
from pyspark.sql.functions import format_number as fmt
from services.text_editor import text_editor_service
import findspark
import shutil
import os

def start_session():
    findspark.init()
    spark = SparkSession \
        .builder \
        .appName("SimpleApplication") \
        .getOrCreate()
    return spark

def get_spark_info(session, text):

    text = text_editor_service.remove_punctuation(text)
    input_file = session.sparkContext.parallelize([text])

    prepared = input_file.map(lambda x: ([x]))
    df = prepared.toDF()
    prepared_df = df.selectExpr('_1 as text')

    # Разбить на токены
    tokenizer = Tokenizer(inputCol='text', outputCol='words')
    words = tokenizer.transform(prepared_df)

    # Удалить стоп-слова
    stop_words = StopWordsRemover.loadDefaultStopWords('russian')
    remover = StopWordsRemover(inputCol='words', outputCol='filtered', stopWords=stop_words)
    filtered = remover.transform(words)
    filtered_words = [row for row in filtered.collect()[0].asDict()['filtered'] if row != '']

    # Посчитать значения TF
    vectorizer = CountVectorizer(inputCol='filtered', outputCol='raw_features').fit(filtered)
    featurized_data = vectorizer.transform(filtered)
    featurized_data.cache()
    vocabulary = [row for row in vectorizer.vocabulary[:11] if row != '']


    # Посчитать значения DF
    # idf = IDF(inputCol='raw_features', outputCol='features')
    # idf_model = idf.fit(featurized_data)
    # rescaled_data = idf_model.transform(featurized_data)

    # Построить модель Word2Vec
    word2Vec = Word2Vec(vectorSize=125, minCount=0, inputCol='words', outputCol='result')
    model = word2Vec.fit(words)
    save_model(model)
    return filtered_words, vocabulary


def save_model(model):
    path = f'{os.getcwd()}/data/v2w_model'
    if os.path.exists(path):
        shutil.rmtree(f'{os.getcwd()}/data/v2w_model')
    model.save('data/v2w_model')


def find_synonyms(word):
    model = Word2VecModel.load("data/v2w_model/")
    print(model)
    df = model.findSynonyms(word, 10).select("word", fmt("similarity", 5).alias("similarity"))
    synonyms_dict = dict((row.asDict()['word'], row.asDict()['similarity']) for row in df.collect())
    return synonyms_dict
