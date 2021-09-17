# 实现银行相关的简单功能
import random

info = '''
                            ***********************************
                            *               中国银行                *
                            *             账户管理系统             *
                            *                   V1.0                *
                            ***********************************
                            *   1.开户                               *
                            *   2.存钱                              *
                            *   3.取钱                               *
                            *   4.转账                              *
                            *   5.查询                              *
                            *   6.退出                              *
                            ***********************************
'''
print(info, end=" ")
bank = {}


# 添加用户
def bank_add(account, username, password, country, province, street, door, money):
    if account in bank:
        return 2
    if len(bank) >= 100:
        return 3
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": "中国银行昌平分行"
    }
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
                      bank[account]["money"], bank[account]["bank_name"]))
    if result == 2:
        print("用户已存在")
    if result == 3:
        print("数据库已满")


# 用户存钱
def saveM(account, money):
    if account in bank:
        bank[account]["money"] += money
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
        print("存入现金成功,账户余额为：{0}".format(bank[account]["money"]))
    else:
        print("账户不存在")


# 用户取钱
def withdrawM(account, password, money):
    if account in bank:
        if bank[account]["password"] == password:
            if bank[account]["money"] >= money:
                bank[account]["money"] -= money
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
        print("成功取出{0}元，账户余额为：{1}".format(money, bank[account]["money"]))
    elif rt == 1:
        print("账号不存在")
    elif rt == 2:
        print("密码错误")
    else:
        print("账户余额不足")


# 用户转账
def transfer(accountOut, accountIn, password, money):
    if accountOut in bank:
        if accountIn in bank:
            if bank[accountOut]["password"] == password:
                if bank[accountOut]["money"] >= money:
                    bank[accountOut]["money"] -= money
                    bank[accountIn]["money"] += money
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
                    print("转账成功，转出账户当前余额为{0}元，转入账户当前余额为{1}".format(bank[accountOut]["money"], bank[accountIn]["money"]))
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
    if account in bank:
        if bank[account]["password"] == password:
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
            print(info % (bank[account]["username"], account, bank[account]["country"], bank[account]["province"],
                          bank[account]["street"], bank[account]["door"], bank[account]["money"],
                          bank[account]["bank_name"]))
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
    try:
        begin = int(input("请选择业务："))
        if begin == 1:
            adduser()
        elif begin == 2:
            getSaveIn()
        elif begin == 3:
            getWithdraw()
        elif begin == 4:
            getTrans()
        elif begin == 5:
            getInqu()
        elif begin == 6:
            break
        else:
            print("请输入0~6之间的数字！")
            continue
    except:
        print("输入错误,请重新输入！")
