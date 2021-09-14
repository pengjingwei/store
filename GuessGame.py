# 起始资充钱 1000  （账户原有资金+刚充值的资金）10%  2000 20%   每猜一次-500一直执行
# 游戏开始按1   退出游戏Q
# 资金为0 锁死系统
# 5次猜对，5次机会用光了就退出
import random
funds = 0  # 账户初始资金
num = input("请填写充值资金：")
count = int(num)
if count > 1000:
    funds = count + count // 1000 * 100
else:
    funds += count
# print(funds)
while funds >= 500:  # 充值资金，资金大于等于500才能进入游戏
    freq = 5  # 5次猜测机会
    while True:
        key = input("输入1进入游戏，输入Q退出游戏：")
        if key == "1":
            if funds <= 0:
                print("资金不足，退出游戏。")
                break
            funds -= 500
            freq -= 1
            ran = random.randint(0, 99)
            guessnum = int(input("请输入猜测的数字："))
            if guessnum == ran:
                print("猜对了，你真棒")
            else:
                print("你猜错了,数字是：{0}".format(ran))
            if freq <= 0:
                print("您的机会不足")
                break
        elif key == "Q" or key == "q":
            break
        else:  # 输入其他字符重新开始循环
            continue
    if funds == 0:
        print("资金为0，系统锁死")
        break
    nextgame = input("按n充值金额，否则退出系统：")
    if nextgame == "n" or nextgame == "N":
        num = input("请填写充值资金：")
        count = int(num)
        if count > 1000:
            funds = count + count // 1000 * 100
        else:
            funds += count
    else:
        break
