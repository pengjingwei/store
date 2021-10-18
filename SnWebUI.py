from time import sleep

from selenium import webdriver
# 创建一个浏览器对象
driver = webdriver.Chrome()
# 访问苏宁易购
driver.get('https://www.suning.com')
# 最大化窗口
driver.maximize_window()
# 设置隐式等待
driver.implicitly_wait(5)
# 定位搜索框，并输入小米11Pro
driver.find_element('id', 'searchKeywords').send_keys('小米11Pro')
# 定位搜索按钮并点击
driver.find_element('id', 'searchSubmit').click()
# 定位搜索到一个的商品并点击
driver.find_element('id', 'ssdsn_search_pro_baoguang-1-0-1_1_01:0000000000_12263716605').click()
# 获取所有句柄并且换到购物句柄页面
handles = driver.window_handles
driver.switch_to.window(handles[1])
# 定位加入购物车按钮，并点击
driver.find_element('id', 'addCart').click()
# 定位去购物车结算按钮，并点击
driver.find_element('xpath', '//*[@name="cart1_go"]').click()
# 释放资源
sleep(10)
driver.quit()
