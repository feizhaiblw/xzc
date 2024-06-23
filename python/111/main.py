from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

wd = webdriver.Edge()
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
select = Select(wd.find_element(By.ID, 'ss_single'))
select.select_by_value("小江老师")

input()
