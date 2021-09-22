# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据
def count(*list):
    dict = {}
    setL = set(list)
    for i in range(len(setL)):
        view = setL.pop()
        dict[view] = list.count(view)
    return dict


# a = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
print("请输入纯数字列表：")
a = list(map(int, input().split()))
dict = count(*a)
print(dict)
