import re
import requests

a = input().split()  # от бота мы получаем название
count = 0
tovar = 'konsol'  # от бота мы получаем консоль это или видеокарта
s = "+".join(a)
url = f'https://www.citilink.ru/search/?text='
url += s
response = requests.get(url)
b = re.findall(r'(https?://\S+)', response.text)
all_urls = []
for i in b:
    if tovar == 'konsol':
        if 'product' in i and 'add' not in i and 'konsol' in i:
            all_urls.append(i.split('"')[0])
    elif tovar == 'pk':
        if 'product' in i and 'add' not in i and 'videokarta' in i:
            all_urls.append(i.split('"')[0])
for i in all_urls:
    if count >= 3:
        break
    abc = requests.get(i)
    if 'InStock' in abc.text:
        print(i)  # вывод ботом
if count == 0:
    print("Сейчас такого товара в наличии нет")  # вывод ботом
