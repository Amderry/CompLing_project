import re
import string


def normalize_text(text):
    text = re.compile(r'[\n\r\t]').sub(" ", text)
    text = text.replace('\xa0', ' ')
    return text


def remove_punctuation(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


