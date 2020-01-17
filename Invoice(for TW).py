import requests
from bs4 import BeautifulSoup

month=str(input("請輸入月份："))
res=requests.get('https://invoices.com.tw/'+month+'.html')
res.encoding='utf-8'
soup=BeautifulSoup(res.text, "html.parser")

x=soup.findAll("td", {"colspan":"3"})[2].get_text().split()
print("領獎期間："+x[2]+x[3]+x[4])

name=soup.findAll("td", {"class":"item", "width":"53"})
Lst=[]
for i in range(len(name)-7):
  x=name[i].get_text()
  Lst.append(x)

num=soup.findAll("td", {"class":"number", "width":"200"})
Lst_2=[]
for j in num:
  y=j.get_text().split()
  Lst_2+=y

print("1. "+Lst[0]+"："+Lst_2[0])
print("2. "+Lst[1]+"："+Lst_2[1])
print("3. "+Lst[2]+"："+Lst_2[2]+ " / "+ Lst_2[3]+" / "+ Lst_2[4])
num=soup.find("td", {"class":"number3"})
small=num.get_text().replace("、", " / ")
print("4. "+Lst[3]+"："+small)

while True:
    a=str(input("請輸入發票數字碼："))
    if a =="e" or a=="E":
        break
    if a == Lst_2[0]:
        print("中特別獎1,000萬元")
        continue
    elif a == Lst_2[1]:
        print("中特獎2,00萬元")
        continue
    elif a == Lst_2[2] or a == Lst_2[3] or a == Lst_2[4]:
        print("中頭獎20萬元")
        continue
    elif a[-7:]==(Lst_2[2][1:8]) or a[-7:]==(Lst_2[3][1:8]) or a[-7:]==(Lst_2[4][1:8]):
        print("中頭獎4萬元")
        continue
    elif a[-6:]==(Lst_2[2][2:8]) or a[-6:]==(Lst_2[3][2:8]) or a[-6:]==(Lst_2[4][2:8]):
        print("中三獎1萬元")
        continue
    elif a[-5:]==(Lst_2[2][3:8]) or a[-5:]==(Lst_2[3][3:8]) or a[-5:]==(Lst_2[4][3:8]):
        print("中四獎4千元")
        continue
    elif a[-4:]==(Lst_2[2][4:8]) or a[-4:]==(Lst_2[3][4:8]) or a[-4:]==(Lst_2[4][4:8]):
        print("中五獎1千元")
        continue
    elif a[-3:]==(Lst_2[2][5:8]) or a[-3:]==(Lst_2[3][5:8]) or a[-3:]==(Lst_2[4][5:8]):
        print("中六獎200元")
        continue
    elif a[-3:]==(small[-3:]) or a[-3:]==(small[-9:-6]) or a[-3:]==(small[:3]):
        print("中增開六獎200元")
        continue
