import urllib3
import requests
from bs4 import BeautifulSoup

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
_res=Res.post('https://www.ptt.cc/ask/over18', verify=False, data=bypass)



target=str(input("請輸入想要找尋的版面："))


_res=Res.get("https://www.ptt.cc/bbs/"+str(target)+"/index.html", verify=False,)
soup1=BeautifulSoup(_res.text)
index_num=soup1.find_all("a", class_="btn wide")
lst=[]
for i in index_num:
  b=i.get("href")
  lst.append(b)
print("總共有："+lst[1].replace(".html","").replace("/bbs/","").replace("/index","").replace(target,"")+"頁數")

start=lst[1].replace(".html","").replace("/bbs/","").replace("/index","").replace(target,"")

end=int(input("終點資料："))
print()

for num in range(int(start)+1, end, -1):
  res=Res.get("https://www.ptt.cc/bbs/"+str(target)+"/index"+str(num)+".html", verify=False)
  res.encoding='utf-8'
  soup=BeautifulSoup(res.text)
  
  
  Title=soup.find_all("div", class_="title")          # 逐一列出超連結
  lst=[]
  for i in Title:
    a=i.find_all("a")
    for j in a:
      href=j.get("href")
      lst.append(href)

  del lst[-4:]                       # 刪除公告項目的連結


  lst_len=len(lst)  
  
  for i in range(lst_len):
    lst[i]                                     # 逐一列出所有連結，並爬取
    new_res=Res.get("https://www.ptt.cc/"+lst[i], verify=False)
    new_res=Res.get("https://www.ptt.cc/"+lst[i], verify=False)
    new_res.encoding='utf-8'
    soup=BeautifulSoup(new_res.text)
    content=soup.find(id="main-content").text
    target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
    content = content.split(target_content)
    print(content[0])
    print("__________________________________________________________________________________","\n")
  

