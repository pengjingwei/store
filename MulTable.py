# 使用while循环实现九九乘法表的打印
print("正序打印")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{0}*{1}={2}".format(j,i,j*i),end=" ")
        j += 1
    i += 1
    print("")

    # 逆序打印
print("逆序打印")
x = 9
while x > 0:
    y=1
    while y <= x:
        print("{0}*{1}={2}".format(y, x, y * x), end=" ")
        y += 1
    x -= 1
    print("")
