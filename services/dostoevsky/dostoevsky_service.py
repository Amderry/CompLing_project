from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


def get_sentiment(text):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    messages = [text]

    results = model.predict(messages, k=2)
    response = {}
    for guess in results[0].keys():
        if guess == 'neutral' or guess == 'speech':
            response['нейтрально'] = str(round(results[0][guess] * 100)) + '%'
        elif guess == 'negative':
            response['негативно'] = str(round(results[0][guess] * 100)) + '%'
        elif guess == 'positive':
            response['положительно'] = str(round(results[0][guess] * 100)) + '%'
    return response


