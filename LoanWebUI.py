# 实现前程贷项目：
#  注册
#  认证：（实名认证，修改手机号，修改登陆密码）
#  添加银行卡
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://8.129.91.152:8765/')

driver.maximize_window()

driver.implicitly_wait(10)

# 注册
driver.find_element('link text', '免费注册').click()

driver.find_element('id', 'phone').send_keys('13695246311')
sleep(10)

driver.find_element('link text', '获取短信验证码').click()

text = driver.find_element('xpath', '//*[@id="layui-layer1"]/div').text

sleep(1)
driver.find_element('xpath', '//input[@name="code"]').send_keys(text[-4:])

driver.find_element('xpath', '//*[@name="password"]').send_keys('gdk123456')

driver.find_element('xpath', '//*[@name="agree"]').click()

driver.find_element('xpath', '//*[text()="下一步"]').click()

driver.find_element('link text', '加入蜂群').click()

# 修改个人信息
driver.find_element('xpath', '/html/body/div/div[1]/div/div[2]/span[3]/a').click()

driver.find_element('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a').click()

driver.find_element('xpath', '//*[text()="实名认证"]').click()

driver.find_element(
    'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[1]/div/input').send_keys('符丹峰')

driver.find_element(
    'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[2]/div/input'
).send_keys('410106199303132512')
driver.find_element(
    'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[3]/div/button').click()

# 修改手机号,手机验证码无法获取
# try:
#     driver.find_element('xpath', '/html/body/div/div[3]/div[1]/ul/li[2]/a').click()
#     driver.find_element('xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[1]/a').click()
# except Exception:
#     driver.find_element('xpath', '/html/body/div/div[3]/div[1]/ul/li[2]/a').click()
#     driver.find_element('xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[1]/a').click()

# 修改密码
try:
    driver.find_element('xpath', '/html/body/div/div[3]/div[1]/ul/li[4]/a').click()
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[1]/input'
    ).send_keys('gdk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[2]/input'
    ).send_keys('gbk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[3]/input'
    ).send_keys('gbk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[5]/button[1]'
    ).click()
except Exception:
    driver.find_element('xpath', '/html/body/div/div[3]/div[1]/ul/li[4]/a').click()
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[1]/input'
    ).send_keys('gdk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[2]/input'
    ).send_keys('gbk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[3]/input'
    ).send_keys('gbk123456')
    driver.find_element(
        'xpath', '//*[@id="layui-layer1"]/div[2]/div/form/div[5]/button[1]'
    ).click()

sleep(5)
driver.quit()
