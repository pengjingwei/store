# 滑动条验证

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'C:\Users\gamer\Desktop\python学习资料\htmls\mousedrag.html')

ele = driver.find_element('xpath', '//*[@id="box"]/div[3]')

ac = ActionChains(driver)

ac.move_to_element_with_offset(ele, 248, 0).perform()
