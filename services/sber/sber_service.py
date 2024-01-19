import requests
def summarize(text):
    sum_response = requests.post('https://api.aicloud.sbercloud.ru/public/v2/summarizator/predict',
                                 json={'instances': [{'text': text, 'num_beams': 5, 'num_return_sequences': 3,
                                                      'length_penalty': 0.5}]}).json()
    return sum_response['prediction_best']['bertscore']

def rewrite(text):
    rewrite_response = requests.post('https://api.aicloud.sbercloud.ru/public/v2/rewriter/predict',
                                 json={'instances': [{'text': text, 'temperature': 0.9, 'top_k': 50,
                                                      'top_p': 0.7, 'range_mode': 'bertscore'}]}).json()
    return rewrite_response['prediction_best']['bertscore']