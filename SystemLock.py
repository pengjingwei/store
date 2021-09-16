# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
import os, time
count = 0
while True:
    if count >= 3:
        print("用户名密码错误三次，系统锁定")
        os.system("pause")
        # time.sleep(1000)
        continue
    userName = input("请输入用户名：")
    if userName == "root":
        passWord = input("请输入密码：")
        if passWord == "admin":
            print("登录成功")
            break
        else:
            count += 1
            print("密码输入错误")
    else:
        count += 1
        print("用户名输入错误")


