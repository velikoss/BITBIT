import re
import requests

a = input().split()
s = "+".join(a)
url = f'https://www.citilink.ru/search/?text='
url += s
response = requests.get(url)
b = re.findall(r'(https?://\S+)', response.text)
all_urls = []
for i in b:
    if 'product' in i and 'add' not in i:
        all_urls.append(i.split('"')[0])
for i in all_urls:
    abc = requests.get(i)
    if 'InStock' in abc.text:
        print(i)