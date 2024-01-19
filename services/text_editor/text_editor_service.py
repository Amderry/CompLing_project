import re
import string
import xml.etree.ElementTree as ET


def normalize_text(text):
    text = re.compile(r'[\n\r\t]').sub(" ", text)
    text = text.replace('\xa0', ' ')
    return text


def remove_punctuation(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def parse_xml(xml):
    xml = xml.decode()
    xml = xml[xml.find('<?xml'):xml.rfind('</document>')] + '</document></fdo_objects>'

    return ET.fromstring(xml)


