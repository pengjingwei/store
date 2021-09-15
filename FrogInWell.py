# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？
wellH = 20
day = 3
night = 2
days=0
while (wellH-3) > 0:
    wellH -= 1
    days += 1
print("需要{0:.2f}天".format(days))