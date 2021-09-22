# 对列表进行冒泡排序
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for j in range(len(a)):
    i = 1
    while i < (len(a) - j):
        if a[i - 1] > a[i]:
            a[i - 1], a[i] = a[i], a[i - 1]
        i += 1
print(a)

