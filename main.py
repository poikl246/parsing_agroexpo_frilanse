import requests
from bs4 import BeautifulSoup
import json
import csv
import os



headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52', 'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}


url = 'https://agroexpo.com/es/catalogo-expositores'
req = requests.get(url, headers=headers)
src = req.text
# print(src)

with open("index.html", "w", encoding='utf-8') as file:
    file.write(src)

# print(src)

with open("index.html") as file:
    src = file.read()


soup = BeautifulSoup(src, 'html.parser')

post = soup.find(class_='post').find(class_='popup').find('div').text.strip()

print(post)
print()
print(post.split('\n'))