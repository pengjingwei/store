# 自动生成测试报告
import unittest

from HTMLTestRunner import HTMLTestRunner

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"E:\PycharmProjects\pythonProject", pattern="Test*.py")

# 2.创建 运行器
src_file = open(file="Calculator.html", mode="w+", encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="加法测试",
    verbosity=1,
    stream=src_file
)
# 3.运行用例
runner.run(tests)
src_file.close()
#  4.邮件发送
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1571933050@qq.com"  # 用户名
mail_pass = "gwbyjndohlulggha"  # 授权码
sender = "1571933050@qq.com"  # 发件人账号
receivcers = ["1571933050@qq.com"]

# 创建一个带附件的实例对象
message = MIMEMultipart()
message['From'] = Header("1571933050@qq.com", "utf-8")
message['To'] = Header("1571933050@qq.com", "utf-8")
subject = '计算器测试'
message['Subject'] = Header(subject, 'utf-8')

send_content = "计算器测试报告"
count_obj = MIMEText(send_content, 'plain', 'utf-8')
message.attach(count_obj)


att1 = MIMEApplication(open("Calculator.html", "rb").read())
att1.add_header('Content-Disposition', 'attachment', filename='Calculator.html')
message.attach(att1)

try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host, 25)
    smtpobj.login(mail_user, mail_pass)
    smtpobj.sendmail(sender, receivcers, message.as_string())
    smtpobj.close()
    print("发送邮件成功")
except smtplib.SMTPException:
    print("发送邮件失败")
