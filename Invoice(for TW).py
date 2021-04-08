import requests
from bs4 import BeautifulSoup
import re


class Invoice:
    def __init__(self, month):
        self.month = month
        self.res=requests.get(f'https://invoices.com.tw/{month}.html')
        self.res.encoding='utf-8' 
        self.bsObj = BeautifulSoup(self.res.text, "html.parser")
    
    def price_list(self): 
        win = self.bsObj.findAll('tr', {'class':"tr"})  
        special = win[0].text.split('\n')[2] 
        jury = win[1].text.split('\n')[1] 
        jackpot = list(map(lambda i: re.sub(r'\s', '', i), win[2].text.split('\n')[1:4]))        
        addit = win[3].text.split('\n')[1].replace("、", ' / ')
        return [special, jury, jackpot, addit]
       
    def show(self):
        title = self.bsObj.find('title').text.split(' ')[0][:4]
        date = self.bsObj.findAll("td", {"colspan":"3"})
        print(f'{title}{self.month[:2]}、{self.month[2:]}月發票', f"領獎時間： {' '.join(date[2].text.split(' ')[2:5])}", f"1. 特別：{self.price_list()[0]}\n2. 特獎：{self.price_list()[1]}\n3. 頭獎：{' / '.join(self.price_list()[2])}\n4. 增開：{self.price_list()[3]}", sep = '\n')
      
    def check(self):
        l = self.price_list()
        while True:
            target = str(input("請輸入發票數字碼："))
            target = re.sub(r'\s', '', target)
            print(target)
            if target == 'e' or target == 'E':
                break
            elif target == l[0]:
                print("中特別獎1,000萬元")    
            elif target == l[1]:
                print("中特獎2,00萬元")
            elif target in l[2]:
                print("中頭獎20萬元")
            elif target[-3:] in l[-1]:
                print("中增開六獎200元")
            elif target[1:] in list(map(lambda i: i[1:], l[2])):
                print("中二獎4萬元")
            elif target[2:] in list(map(lambda i: i[2:], l[2])):
                print("中三獎1萬元")
            elif target[3:] in list(map(lambda i: i[3:], l[2])):
                print("中四獎4千元")
            elif target[4:] in list(map(lambda i: i[4:], l[2])):
                print("中五獎1千元")
            elif target[5:] in list(map(lambda i: i[5:], l[2])):
                print("中六獎200元")

i = Invoice('0102')
i.show()  
i.check()
