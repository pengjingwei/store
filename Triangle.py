# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
print("请输入三角形三边的值：",end="")
side1 = float(input())
side2 = float(input())
side3 = float(input())
sum1 = side1 + side2
sum2 = side2 + side3
sum3 = side1 + side3
s1=side1*side1
s2=side2*side2
s3=side3*side3
if sum1>side3 and sum2>side1 and sum3>side2:
    if side1 == side2 and side2 ==side3:
        print("等边三角形")
    elif side1 == side2 or side1 ==side3 or side2 == side3:
        if s1+s2 == s3 or s1+s3 == s2 or s2 +s3 == s1:
            print("直角三角形")
        print("等腰三角形")
    elif s1+s2 == s3 or s1+s3 == s2 or s2 +s3 == s1:
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("不能形成三角形")