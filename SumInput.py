# 输入10个数字，打印10个数字的和
sum1 = 0
i = 0
print("请输入10个要求和的数字：", end="")
while i < 10:
    a = float(input())  # 每回车一次算是输入一个数字
    sum1 += a
    i += 1
print("10个数的和为：{0:.2f}".format(sum1))

# 输入10个数字，打印10个数字的和，最大值，平均数
sum2 = 0
max1=0
print("请输入10个要求和的数字：", end="")
for x in range(10):
    a = float(input())  # 每回车一次算是输入一个数字
    if a > max1:
        max1 = a
    sum2 += a
everge = sum2 / 10
print("10个数的和为：{0:.2f}，最大值为：{1:.2f}，平均值为：{2:.2f}".format(sum2,max1,everge))
