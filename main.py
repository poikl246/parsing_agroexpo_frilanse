import requests
from bs4 import BeautifulSoup
import json
import csv
import os



with open("page_source.html", encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src, 'html.parser')

poster = soup.find_all(class_='popup')
caunt = 0

itog_file = [['Name', 'Name2', 'Producto', 'Teléfono', 'Ciudad', 'Correo Electrónico', 'Info', 'Sitio Web', 'Ubicación']]

def list_to_str(input_file):
    out_file = ''
    for word in input_file:
        out_file = out_file + str(word)

    return out_file

# file = [name, name2, Producto, Phone, Ciudad, mail, description, Web, location]
for post in poster:

    out = post.find('div').find_all('div')

    out1 = out[0].text.strip().split('\n')
    out2 = out[1].text.strip().split('\n')

    # out = post.find('div').find('h4').next_sibling.next_sibling

    caunt +=1
    # file = [out[0], out[3], out[5], out[7], out[9], out[15], out[17]]

    # name = ''
    # Producto = ''
    # Phone = ''
    # Ciudad = ''
    # mail = ''
    # wed = ''
    # GPS = ''
    # info = ''
    print(out1, out2)

    print()

    if out1[0] != 'Producto':
        name2 = out1[0]
    else:
        name2 = ''

    Producto = list_to_str(out1[out1.index('Producto') + 1: out1.index('Teléfono')])
    Phone = out1[out1.index('Teléfono') + 1]
    Ciudad = out1[out1.index('Ciudad') + 1]
    mail = out1[out1.index('Correo Electrónico') + 1]
    name = out2[0]
    description = list_to_str(out2[0 : out2.index('Sitio Web')])
    Web = out2[out2.index('Sitio Web') + 1]
    location = out2[out2.index('Ubicación') + 1]



    file = [name, name2, Producto, Phone, Ciudad, mail, description, Web, location]
    itog_file.append(file)


with open('exit_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(itog_file)




print(caunt)
