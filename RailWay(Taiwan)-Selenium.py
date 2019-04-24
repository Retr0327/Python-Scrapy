from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('C:/Users/user/chromedriver.exe')    #chromedriver location
driver.get('http://railway.hinet.net/Foreign/TW/etkind1.html')

id=driver.find_element_by_name('person_id')
id.send_keys('Exxxxxxxxxxxx')

selectDate=driver.find_element_by_name('getin_date')
date=Select(selectDate)
date.select_by_visible_text('2019/03/21【四】')    #年/月/日【一~日】

selectFrom=driver.find_element_by_name('from_station')
From=Select(selectFrom)
From.select_by_visible_text('100-台北')

selectTo=driver.find_element_by_name('to_station')
To=Select(selectTo)
To.select_by_visible_text('146-台中')

#100-台北    106-桃園    108-中壢    146-台中   185-高雄

selectStart=driver.find_element_by_name('getin_start_dtime')
Start=Select(selectStart)
Start.select_by_visible_text('00:00')     

selectEnd=driver.find_element_by_name('getin_end_dtime')
End=Select(selectEnd)
End.select_by_visible_text('09:00')     

#00:00~23:00

selectTrain=driver.find_element_by_name('train_type')
train=Select(selectTrain)
train.select_by_visible_text('*1-自強號')

driver.find_element_by_xpath("/html/body[@class='demo-include']/div[@class='container']//form[@action='../common/check_etkind1.jsp']//button[@type='submit']").click()



