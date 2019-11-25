import requests
from bs4 import BeautifulSoup

month=str(input("請輸入月份："))

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res=requests.get('https://invoices.com.tw/'+month+'.html')
res.encoding='utf-8'
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select(".button")[0].text.replace(" ","、").replace("號","號："))


x=soup.find_all("td", class_="number")
b=x[0].text
c=x[1].text
d=x[2].text.split('.')
d=d[0].replace("\n "," / ").replace("\n","")
d1=d[:8]
d2=d[8:16]
d3=d[16:24]
e=soup.select(".number3")[0].text.split('.')
e=e[0].replace('\n',"").replace('、'," / ")

print("1.特別獎："+b)
print("2.特獎："+c)
print("3.頭獎："+d1+" / "+d2+" / "+d3)
print("4.增開六獎："+e)

while True:
    a=str(input("請輸入發票數字碼："))
    if a =="e" or a=="E":
        break
    if a ==(b):
        print("中特別獎1,000萬元")
        continue
    elif a==(c):
        print("中特獎2,00萬元")
        continue
    elif a==(d1) or a==(d2) or a==(d3):
        print("中頭獎20萬元")
        continue
    elif a[-7:]==(d1[1:8]) or a[-7:]==(d2[1:8]) or a[-7:]==(d3[1:8]):
        print("中頭獎4萬元")
        continue
    elif a[-6:]==(d1[2:8]) or a[-6:]==(d2[2:8]) or a[-6:]==(d3[2:8]):
        print("中三獎1萬元")
        continue
    elif a[-5:]==(d1[3:8]) or a[-5:]==(d2[3:8]) or a[-5:]==(d3[3:8]):
        print("中四獎4千元")
        continue
    elif a[-4:]==(d1[4:8]) or a[-4:]==(d2[4:8]) or a[-4:]==(d3[4:8]):
        print("中五獎1千元")
        continue
    elif a[-3:]==(d1[5:8]) or a[-3:]==(d2[5:8]) or a[-3:]==(d3[5:8]):
        print("中六獎200元")
        continue
    elif a[-3:]==(e[-3:]) or a[-3:]==(e[-9:-6]) or a[-3:]==(e[:3]):
        print("中增開六獎200元")
        continue


