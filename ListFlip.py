# 实现列表的数据翻转
List = [1,2,3,4,5,6,7,8,9]
print("[::-1]方式翻转列表：",List[::-1])
l = reversed(List)
print("reversed()方法翻转列表：",list(l))

# 统计列表中的每个数字出现的次数
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
setL = set(List)
# print(setL.pop())
for i in range(len(setL)):
    view = setL.pop()
    print("{0}出现了{1}次。".format(view,List.count(view)))