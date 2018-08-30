#!/usr/bin/python3
import requests, bs4
x = 0
url = 'https://app.famitsu.com/compass-ranking/'
print('1:総合ランキング\n2:使用率ランキング\n3:勝率ランキング')
s = input()
if s == '2':
    print('コンパスの使用率ランキング\n')
    x = 31
elif s == '1':
    print('コンパスの総合ランキング\n')
    x = 0
else:
    print('コンパスの勝率ランキング\n')
    x = 62

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
link = soup.select('tbody tr td a')
for i in range(5):
    links = link[2+x+i].string
    print('{}位・{}'.format(i+1, links))
