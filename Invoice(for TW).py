import requests
from bs4 import BeautifulSoup
import re

month=str(input("請輸入月份："))
res=requests.get('https://invoices.com.tw/'+month+'.html')
res.encoding='utf-8'
bsObj=BeautifulSoup(res.text, "html.parser")
title=bsObj.find('title').text
date=bsObj.findAll("td", {"colspan":"3"})
win=bsObj.findAll('tr', {'class':"tr"})
print(title.split(' ')[0][:4], f'{month[:2]}、{month[2:]}月發票')
print("領獎時間：", ' '.join(date[2].text.split(' ')[2:5]))
special=win[0].text.split('\n')[2]
jury=win[1].text.split('\n')[1] 
jackpot=win[2].text.split('\n')[1:4]
addit=win[3].text.split('\n')[1]
print("1. 特別：", special)
print("2. 特獎：", jury)
print("3. 頭獎：", ' / '.join(jackpot))
print("4. 增開：", addit.replace("、", ' / '), '\n')

while True:
    target=str(input("請輸入發票數字碼："))
    target=re.sub(r'\s', '', target)
    print(target)
    if target =="e" or target=="E":
        break
    if target == special:
        print("中特別獎1,000萬元")
        continue
    elif target == jury:
        print("中特獎2,00萬元")
        continue
    elif target in jackpot:
        print("中頭獎20萬元")
        continue
    elif target[1:] in list(map(lambda i: i[1:], jackpot)):
        print("中二獎4萬元")
        continue
    elif target[2:] in list(map(lambda i: i[2:], jackpot)):
        print("中三獎1萬元")
        continue
    elif target[3:] in list(map(lambda i: i[3:], jackpot)):
        print("中四獎4千元")
        continue      
    elif target[4:] in list(map(lambda i: i[4:], jackpot)):
        print("中五獎1千元")
        continue
    elif target[5:] in list(map(lambda i: i[5:], jackpot)):
        print("中六獎200元")
        continue
    elif target[-3:] in addit.split('、'):
        print("中增開六獎200元")
        continue
