import urllib3
import requests
from bs4 import BeautifulSoup
import re 

urllib3.disable_warnings()
bypass={
    'from':'/bbs/Gossiping/index.html',
    'from':'/bbs/sex/index.html',
    'from':'/bbs/HatePolitics/index.html',
    'from':'/bbs/Boy-Girl/index.html',
    'yes':'yes'
}
Res=requests.session()
res=Res.post('https://www.ptt.cc/ask/over18', verify=False, data=bypass)

x=int(input("請輸入想找多少筆資料："))
for num in range(1, x):
  res=Res.get("https://www.ptt.cc/bbs/sex/index"+str(num)+".html", verify=False,)
res.encoding='utf-8'
soup=BeautifulSoup(res.text)


Title=soup.find_all("div", class_="title")          # 獲取超連結
lst=[]
for i in Title:
  a=i.find_all("a")
  for j in a:
    href=j.get("href")
    lst.append(href)

del lst[-4:]                       #刪除公告項目


lst_len=len(lst)                         

for i in range(lst_len):
  lst[i]                                     # 逐一列出所有連結
  new_res=Res.get("https://www.ptt.cc/"+lst[i], verify=False)
  new_res=Res.get("https://www.ptt.cc/"+lst[i], verify=False,)
  new_res.encoding='utf-8'
  soup=BeautifulSoup(new_res.text)
  main=soup.select("#main-content")
  [s.extract() for s in soup('span', class_='f2')]
  [s.extract() for s in soup('span', class_='f6')]
  [s.extract() for s in soup('div', class_='push')]
  [s.extract() for s in soup('span', class_='push-ipdatetime')]
  print(main[0].text)
  print("__________________________________________________________________________________")