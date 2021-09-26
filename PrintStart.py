# 打印*阵图

for i in range(7):
    j = 50-i
    t = i+1
    while j > 0:
        print("", end=" ") # 每行打印j个空格
        j -= 1
    while t > 0:
        print("*", end=" ")  # 每行打印i+1个*
        t -= 1
    print("")  # 换行


