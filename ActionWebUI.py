# 滑动条验证
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'C:\Users\gamer\Desktop\python学习资料\htmls\mousedrag.html')

ele = driver.find_element('xpath', '//*[@id="box"]/div[3]')
# 创建事件链
ac = ActionChains(driver)
# 将鼠标移动到要移动的元素上面
ac.move_to_element(ele)
# 点击元素并保持
ac.click_and_hold().perform()
# 移动一直点击元素
ac.move_to_element_with_offset(ele, 240, 0).perform()
# 释放点击
ac.release(ele)
sleep(5)
driver.quit()
