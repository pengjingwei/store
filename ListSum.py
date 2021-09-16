# 其中是5的倍数的和
a=[1,5,21,30,15,9,30,24]
suma=0
for i in range(len(a)):
    if a[i] % 5 == 0:
        suma += a[i]
print("和为：{0}".format(suma))