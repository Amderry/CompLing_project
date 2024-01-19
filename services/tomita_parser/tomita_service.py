from services.db import context
from services.text_editor import text_editor_service
import os
import subprocess
import xml.etree.ElementTree as ET

def attach_persons_to_dict():
    full_names = [vip.name for vip in context.get_vip_persons()]
    #reversed_full_names = [vip.name.split()[1] + ' ' + vip.name.split()[0] for vip in context.get_vip_persons()]
    surnames_only = [vip.name.split()[0] for vip in context.get_vip_persons()]
    names_only = set(str(vip.name.split()[-1]) for vip in context.get_vip_persons())
    #full_names = full_names + surnames_only + reversed_full_names

    # with open(f'{os.getcwd()}/data/tomita_data/vip/vipdic.gzt', 'a+') as file:
    #     file.write(f'key = {[name for name in full_names]}')
    snames = str([name for name in surnames_only])[1:-1].replace(',', ' |')
    names = str([name for name in names_only])[1:-1].replace(',', ' |')
    print(f'\tkey = {snames}')
    print(f'\tkey = {names}')


def attach_sights_to_dict():
    sights = [sight.name for sight in context.get_sights()]

    sights = str([sight for sight in sights])[1:-1].replace(',', ' |')
    # names = str([name for name in names_only])[1:-1].replace(',', ' |')
    print(sights)


def find_vip_persons(text):
    p = subprocess.Popen(f'cd {os.getcwd()}/data/tomita_data/vip && tomita-parser config.proto', stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # p = subprocess.Popen(f'cd /home/victor/CompLing_project/data/tomita_data/vip && tomita-parser config.proto',
    #                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output = p.communicate(input=text.encode())[0]

    xml = text_editor_service.parse_xml(output)

    vip_persons = set()
    for table in xml.iter('VipPerson'):
        vip_person = str()
        for child in table:
            vip_person += child.attrib['val'].capitalize() + ' '

        vip_persons.add(vip_person[:-1])

    return vip_persons


def find_sights(text):
    p = subprocess.Popen(f'cd {os.getcwd()}/data/tomita_data/sight && tomita-parser config.proto',
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # p = subprocess.Popen(f'cd /home/victor/CompLing_project/data/tomita_data/sight && tomita-parser config.proto',
    #                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output = p.communicate(input=text.encode())[0]
    xml = text_editor_service.parse_xml(output)
    sights = set()
    for table in xml.iter('Sight'):
        sight = str()
        for child in table:
            sight += child.attrib['val'].capitalize() + ' '
        sights.add(sight[:-1])
    return sights

# print(find_vip_persons(context.get_page_info('https://bloknot-volgograd.ru/news/v-gory-musora-i-besprolaznuyu-gryaz-tknuli-nosom-ch-1676138').text))
# print(find_sights(context.get_page_info('https://bloknot-volgograd.ru/news/na-mamaevom-kurgane-v-volgograde-svyashchennik-ven-1564514').text))