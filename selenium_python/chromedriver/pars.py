import random
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv
import os


with open("../../page_source.html", encoding='utf-8') as file:
    src = file.read()

# print(src)
soup = BeautifulSoup(src, 'html.parser')

vopros = soup.find('div', class_='problem').find_all(class_='wrapper-problem-response')

# print(vopros)
# print('#'*20)
list_utog = []
for vop in vopros:
    try:
        # print(vop.get('aria-label'))
        name_vopros = vop.find(class_='response-fieldset-legend field-group-hd').text
        vopr_list = vop.find_all(class_="field")

        list_otvet = []
        for vo in vopr_list:
            otvet = vo.find(class_='response-label field-label label-inline')
            # print(otvet.get('id'), str(otvet.text).replace('\n', '').strip())

            list_otvet.append([otvet.get('id'), str(otvet.text).replace('\n', '').strip()])

        # print(name_vopros)
        list_utog.append([name_vopros, list_otvet])

    except:
        print('Есть ошибка')

print(list_utog[0][1][3])