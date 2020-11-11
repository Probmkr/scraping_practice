import requests as req
from bs4 import BeautifulSoup as beasou

res = req.get('https://edogawa.schoolweb.ne.jp/swas/index.php?id=1320062&frame=frm4cd2692acc0d6')
soup = beasou(res.text, 'html.parser')

first_type = soup.select('ul.first-of-type')[0]

header = []
for i in range(1, 13): #1番目から12番目まで。つまり、1番目から　13マイナス1　番目まで
    try:
        li = first_type.find(id=f'elm_ni_{str(i).zfill(5)}').find('a')
        header.append(li)
    except:
        break

for i in header:
    print(i.text)
