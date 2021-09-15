# 输入编号，进行点名
nameList = ["西园寺世界", "艾斯德斯", "夜刀神十香", "时崎狂三", "五河琴里", "四系乃", ";雷姆", "2B"]
while True:
    try:
        num = int(input("请输入点名的人的编号："))
        if num < 0 or num >= len(nameList):
            print("请输入0到{0}之间的数".format(len(nameList) - 1))
        if num < len(nameList):
            print(nameList[num])
    except:
        print("请输入一个正整数")
        continue

