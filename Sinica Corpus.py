# In[115]:


from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests
from bs4 import BeautifulSoup
import docx
doc = docx.Document()

driver = webdriver.Chrome('C:/Users/user/chromedriver.exe')    #chromedriver location
driver.get('http://asbc.iis.sinica.edu.tw/index_range.htm')
soup=BeautifulSoup(driver.page_source)
driver.find_element_by_xpath("//body/form[@name='form1']//input[@name='Submit']").click()
# 查詢關鍵字網址: http://asbc.iis.sinica.edu.tw/index2.asp


# In[116]:


target=str(input("請輸入要找尋的文字："))
id=driver.find_element_by_name('inputword')
id.send_keys(target)
driver.find_element_by_xpath("//body/div/table//form[@name='form1']//input[@value='送出']").click()


# In[117]:


# 要分開，要讓driver讀去page source
soup=BeautifulSoup(driver.page_source)


# In[118]:


# 顯示總共有多少筆

print(soup.find_all("p")[-1].text)

page=soup.find_all("p")[-1].text.replace("共有 ","").replace(" 筆資料","")
print("共有",int(page)//100+1," 頁")


# In[119]:


soup=BeautifulSoup(driver.page_source)
left=soup.find_all("div",align="right")           
main=soup.find_all("b")                             # 主要搜尋字詞
right=soup.find_all("td", width="501")
list_len=len(left)
for i in range(list_len):
    left=soup.find_all("div",align="right")
    main=soup.find_all("b")
    right=soup.find_all("td", width="501")
    paragraph=left[i].text.replace('more',''),main[0].text, right[i].text.replace('more','')
    doc.add_paragraph(paragraph)


# In[120]:


driver.find_element_by_xpath("//body/div[2]/a[10]").click()
soup=BeautifulSoup(driver.page_source)
left=soup.find_all("div",align="right")           
main=soup.find_all("b")                             # 主要搜尋字詞
right=soup.find_all("td", width="501")
list_len=len(left)
for i in range(list_len):
    left=soup.find_all("div",align="right")
    main=soup.find_all("b")
    right=soup.find_all("td", width="501")
    paragraph=left[i].text.replace('more',''),main[0].text, right[i].text.replace('more','')
    doc.add_paragraph(paragraph)


# In[121]:


driver.find_element_by_xpath("//body/div[2]/a[11]").click()
soup=BeautifulSoup(driver.page_source)
left=soup.find_all("div",align="right")           
main=soup.find_all("b")                             # 主要搜尋字詞
right=soup.find_all("td", width="501")
list_len=len(left)
for i in range(list_len):
    left=soup.find_all("div",align="right")
    main=soup.find_all("b")
    right=soup.find_all("td", width="501")
    paragraph=left[i].text.replace('more',''),main[0].text, right[i].text.replace('more','')
    doc.add_paragraph(paragraph)


# In[122]:



doc.save(target+'.docx')

