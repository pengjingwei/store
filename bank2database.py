# 实现银行相关的简单功能
import random

import DBUtils

info = '''
                            ***********************************
                            *               中国银行                *
                            *             账户管理系统             *
                            *                   V1.0                *
                            ***********************************
                            *   1.开户                               *
                            *   2.存钱                               *
                            *   3.取钱                               *
                            *   4.转账                               *
                            *   5.查询                               *
                            *   6.退出                               *
                            ***********************************
'''
print(info, end=" ")
bank = {}
BANK_NAME = "中国银行昌平分行"


# 添加用户
def bank_add(account, username, password, country, province, street, door, money):
    sql = "select * from users where account = %s"
    param = [account]
    data = DBUtils.select(sql, param)
    if len(data) > 0:
        return 2

    sql1 = "select count(*) from users"
    param1 = []
    data = DBUtils.select(sql1, param1)
    if len(data) >= 100:
        return 3
    sql2 = "insert into users values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account, username, password, country, province, street, door, money, BANK_NAME]
    DBUtils.updata(sql2, param2)
    return 1


# 获取要添加的用户信息，调用添加用户函数
def adduser():
    account = random.randint(10000000, 1000000000)
    username = input("请输入用户名：")
    password = input("请输入密码：")
    print("请输入您的详细地址：")
    country = input("\t\t国籍：")
    province = input("\t\t省份：")
    street = input("\t\t街道：")
    door = input("\t\t门牌号：")
    money = 0
    result = bank_add(account, username, password, country, province, street, door, money)
    if result == 1:
        print("添加用户成功，以下是您的信息：")
        info = '''
        ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
        '''
        print(info % (username, account, country, province, street, door,
                      money, BANK_NAME))
    if result == 2:
        print("用户已存在")
    if result == 3:
        print("数据库已满")


# 用户存钱
def saveM(account, money):
    sql = "select * from users where account = %s"
    param = [account]
    data = DBUtils.select(sql, param)
    if len(data) > 0:
        sql1 = "select money from users where account = %s"
        param1 = [account]
        data1 = DBUtils.select(sql1, param1)
        lt = []
        for s in data1:
            lt.append(s[0])
        lt[0] += money
        # print(data1)
        sql2 = "update users set money = %s where account = %s"
        param2 = [lt[0], account]
        DBUtils.updata(sql2, param2)
        return True
    else:
        return False


# 获取存钱的账户信息
def getSaveIn():
    account = input("请输入要存入金额的账户：")
    money = input("请输入要存入的金额：")
    # print(account)
    if account.isdigit():
        account = int(account)
        if money.isdigit():
            money = int(money)
        else:
            print("请输入正确的金额！")
    else:
        print("账户输入错误！")
    rt = saveM(account, money)
    if rt:
        sql = "select money from users  where account = %s"
        param = [account]
        data = DBUtils.select(sql,param)
        lt = []
        for s in data:
            lt.append(s[0])
        print("存入现金成功,账户余额为：{0}".format(lt[0]))
    else:
        print("账户不存在")


# 用户取钱
def withdrawM(account, password, money):
    sql = "select * from users where account = %s"
    param = [account]
    data = DBUtils.select(sql, param)
    if len(data) > 0:
        sql1 = "select * from users where account = %s and password = %s"
        param1 = [account, password]
        data1 = DBUtils.select(sql1, param1)
        if len(data1):
            sql2 = "select money from users where account = %s"
            param2 = [account]
            data2 = DBUtils.select(sql2, param2)
            lt = []
            for s in data2:
                lt.append(s[0])
            if lt[0] >= money:
                sql3 = "update users set money = %s"
                lt[0] -= money
                param3 = [lt[0]]
                DBUtils.updata(sql3, param3)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 获取取钱账户信息
def getWithdraw():
    account = input("请输入要提取金额的账户：")
    password = input("请输入本账户密码：")
    money = input("请输入要提取的金额：")
    if account.isdigit():
        account = int(account)
        if money.isdigit():
            money = int(money)
        else:
            print("请输入正确的金额！")
    else:
        print("账户输入错误！")
    rt = withdrawM(account, password, money)
    if rt == 0:
        sql = "select money from users  where account = %s"
        param = [account]
        data = DBUtils.select(sql, param)
        lt = []
        for s in data:
            lt.append(s[0])
        print("成功取出{0}元，账户余额为：{1}".format(money, lt[0]))
    elif rt == 1:
        print("账号不存在")
    elif rt == 2:
        print("密码错误")
    else:
        print("账户余额不足")


# 用户转账
def transfer(accountOut, accountIn, password, money):
    sql = "select * from users where account = %s"
    param = [accountOut, accountOut]
    data = DBUtils.select(sql, param[0])
    if len(data) > 0:
        data1 = DBUtils.select(sql, param[1])
        if len(data1) > 0:
            sql1 = "select * from users where account = %s and password = %s"
            param1 = [accountOut, password]
            data2 = DBUtils.select(sql1, param1)
            if len(data2) > 0:
                sql3 = "select money from users where account = %s"
                param3 = [accountOut, accountIn]
                lt = []
                data3 = DBUtils.select(sql3, param3[0])
                data4 = DBUtils.select(sql3,param3[1])
                for s in data3:
                    lt.append(s[0])
                for s in data4:
                    lt.append(s[0])
                if lt[0] >= money:
                    lt[0] -= money
                    lt[1] += money
                    sql4 = "update users set money = %s where account = %s"
                    param4 = [lt[0], accountOut]
                    param5 = [lt[1], accountIn]
                    DBUtils.updata(sql4, param4)
                    DBUtils.updata(sql4, param5)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 1


# 获取转账相关信息，调用转账函数
def getTrans():
    accountOut = input("请输入转出金额的账户：")
    accountIn = input("请输入转入金额的账户：")
    password = input("请输入转出金额账户的密码：")
    money = input("请输入转出的金额")
    if accountOut.isdigit():
        accountOut = int(accountOut)
        if accountIn.isdigit():
            accountIn = int(accountIn)
            if money.isdigit():
                money = int(money)
                rt = transfer(accountOut, accountIn, password, money)
                if rt == 0:
                    sql = "select money from users  where account = %s"
                    param = [accountOut,accountIn]
                    data = DBUtils.select(sql, param[0])
                    data1 = DBUtils.select(sql, param[1])
                    lt = []
                    for s in data:
                        lt.append(s[0])
                    for s in data1:
                        lt.append(s[0])
                    print("转账成功，转出账户当前余额为{0}元，转入账户当前余额为{1}".format(lt[0], lt[1]))
                elif rt == 1:
                    print("转入或转出的账号不存在")
                elif rt == 2:
                    print("输入的密码不正确")
                else:
                    print("账户余额不足")
            else:
                print("请输入正确的金额！")
        else:
            print("请按格式输入正确的账户！")
    else:
        print("请按格式输入正确的账户！")


# 查询账户信息
def inquire(account, password):
    sql = "select * from users where account = %s"
    param = [account]
    data = DBUtils.select(sql, param)
    if len(data) > 0:
        sql1 = "select * from users where account = %s and password = %s"
        param1 = [account, password]
        data1 = DBUtils.select(sql1, param1)
        print(data1)
        lt = []
        for i in data1[0]:
            lt.append(i)
        print(lt)
        if len(lt) > 0:
            info = '''
            ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
            '''
            print(info % (lt[1], account,lt[3], lt[4], lt[5], lt[6], lt[7],BANK_NAME))
        else:
            print("密码输入错误！")
    else:
        print("账户不存在")


# 获取查询账户的信息，并调用查询函数
def getInqu():
    account = input("请输入要查询的账户：")
    password = input("请输入要查询账户的密码：")
    if account.isdigit():
        account = int(account)
        inquire(account, password)
    else:
        print("请输入正确格式的账户！")


while True:
    begin = input("请选择业务：")
    if begin == "1":
        adduser()
    elif begin == "2":
        getSaveIn()
    elif begin == "3":
        getWithdraw()
    elif begin == "4":
        getTrans()
    elif begin == "5":
        getInqu()
    elif begin == "6":
        break
    else:
        print("请输入0~6之间的数字！")
        continue
