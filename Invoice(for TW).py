import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res=requests.get('https://invoices.com.tw/0102.html')
res.encoding='utf-8'
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select(".button")[0].text.replace(" ","、").replace("號","號："))

x=soup.find_all("td", class_="number")
b=x[0].text
c=x[1].text
d=x[2].text.split('.')
d=d[0].replace("\n "," / ").replace("\n","")
e=soup.select(".number3")[0].text.split('.')
e=e[0].replace("ã"," / ")

print("1.特別獎："+b)
print("2.特獎："+c)
print("3.頭獎："+d)
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
    elif a==(d[-8:]) or a==(d[-19:-11]) or a==(d[-30:-22]):
        print("中頭獎20萬元")
        continue
    elif a[-7:]==(d[-7:]) or a[-7:]==(d[-18:-11]) or a[-7:]==(d[-29:-22]):
        print("中頭獎4萬元")
        continue
    elif a[-6:]==(d[-6:]) or a[-6:]==(d[-17:-11]) or a[-6:]==(d[-28:-22]):
        print("中三獎1萬元")
        continue
    elif a[-5:]==(d[-5:]) or a[-5:]==(d[-16:-11]) or a[-5:]==(d[-27:-22]):
        print("中四獎4千元")
        continue
    elif a[-4:]==(d[-4:]) or a[-4:]==(d[-15:-11]) or a[-4:]==(d[-26:-22]):
        print("中五獎1千元")
        continue
    elif a[-3:]==(d[-3:]) or a[-3:]==(d[-14:-11]) or a[-3:]==(d[-25:-22]):
        print("中六獎200元")
        continue
    elif a[-3:]==(e[-3:]) or a[-3:]==(e[-11:-8]):
        print("中增開六獎200元")
        continue