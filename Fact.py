# 实现20以内的数的阶乘
i = 0
fact = 1
while i <= 20:
    if i == 0:
        fact = 1
        i += 1
        print("{0}的阶乘为：{1}".format(i, fact))
        continue
    if i == 1:
        fact = 1
        i += 1
        print("{0}的阶乘为：{1}".format(i, fact))
        continue
    j = i
    while j >= 2:
        fact = fact * j
        j -= 1
    print("{0}的阶乘为：{1}".format(i, fact))
    i += 1
