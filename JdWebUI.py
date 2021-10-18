# 访问京东商城，搜索商品并查看商品详情
from time import sleep

from selenium import webdriver

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问京东商城
driver.get("https://www.jd.com")

# 最大化浏览器
driver.maximize_window()

# 设置隐式等待
driver.implicitly_wait(5)

# 在搜索框中输入查找的内容
driver.find_element('id', 'key').send_keys("外星人ALIENWARE")

# 点击搜索按钮
driver.find_element('xpath', '//button[@aria-label="搜索"]').click()

# 点击一个商品
driver.find_element('xpath', '//*[@id="J_goodsList"]/ul/li[2]/div/div[1]/a').click()

# 获取所有句柄，切换句柄
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 释放资源
sleep(5)
driver.quit()
