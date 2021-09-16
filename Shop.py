# 需求：
# 购物流程。
# 商品在货架上
# 空的购物车
# 自己的初始化资金
# 任务：
# 10张老干妈：7折优惠券，20张联想电脑1折优惠券
# 开始买东西之前，提示是否要抽一张优惠券。
# 若是：随机给一张，最终要进行使用优惠券的进行结算。
# 若否：正常买东西
import  random
shop = [
    ["劳力士手表", 200000],
    ["Iphone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["HUA WEI WATCH", 1200],
    ["Mac PC", 15000],
    ["辣条", 2.5],
    ["老干妈", 13]
]
mycart = []
tickets = ["老干妈","lenovo"]
i = 10
j = 20
try:
    money = float(input("请输入您的余额："))
    for key,value in enumerate(shop):
        print(key,value)
    while True:
        ticket = input("是否要抽取一张优惠卷：Y/N ")
        choose = input("请输入你想要购买的商品的编号：")
        if choose.isdigit():
            choose = int(choose)
            if choose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                if money > shop[choose][1]:
                    mycart.append(shop[choose])
                    if ticket == "Y" or ticket == "y":
                        if i <= 0 and j <= 0:
                            print("优惠券已用完")
                            continue
                        discount = random.choice(tickets)  # 从老干妈，联想优惠卷中抽取一张
                        print("恭喜您抽中{0}的优惠卷".format(discount))
                        if discount == "lenovo" and choose == 2:
                            i -= 1
                            money = money - shop[choose][1] * 0.1
                        elif choose == 6:
                            j -= 1
                            money = money - shop[choose][1] * 0.7
                        else:
                            money -= shop[choose][1]
                    else:
                        money -= shop[choose][1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                else:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
        elif choose == "q" or choose == "Q":
            print("拜拜了，您嘞！欢迎下次光临！")
            break
        print("以下是您的购物小条，请拿好：")
        for key, value in enumerate(mycart):
            print(key, value)
        print("本次余额还剩：{0}￥".format(money))
except:
    print("输入有误，请重新输入！")

