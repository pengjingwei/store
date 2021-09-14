# 使用+，-号实现两个数的调换。
print("请输入两个数字：")
num1 = float(input())
num2 = float(input())
change = num1 - num2
num1=num1-change
num2=num2+change
print("现在第一个值为：{0:.2f}，第二个值为：{1:.2f}".format(num1,num2))
