import re
import requests
import sqlite3

a = input()  # от бота мы получаем название
aa = a.split()
count = 0
tovar = 'pk'  # от бота мы получаем консоль это или видеокарта
s = "+".join(aa)
url = f'https://www.citilink.ru/search/?text='
url += s
response = requests.get(url)
b = re.findall(r'(https?://\S+)', response.text)
all_urls = []
name_telegram = '@TEAM_LEAD'  # тег пользователя
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
        count += 1
if count == 0:
    print("Сейчас такого товара в наличии нет")  # вывод ботом
    name = 'products_search.db'
    con = sqlite3.connect(name)
    cur = con.cursor()
    result = cur.execute(f"""INSERT INTO all_products
                          (name_telegram, need_products)
                          VALUES
                          ('{name_telegram}', '{a}');""").fetchall()
    con.commit()
    con.close()
