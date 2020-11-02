import requests
from bs4 import BeautifulSoup

def rf(num):
    for _ in range(num):
        print()

def line(num):
    print('-'*num)

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
txt = res.text

soup = BeautifulSoup(txt, "html.parser")
item = soup.select('div .books')
print(item)
rf(19)
line(70)
rf(3)
for i in item:
    print(i)
    rf(3)
    line(70)
    rf(3)


