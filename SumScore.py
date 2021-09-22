# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
r1 = {"name": "罗恩", "score": [23, 35, 44]}
r2 = {"name": "哈利", "score": [60, 77, 68, 88, 90]}
r3 ={"name": "赫敏", "score": [97, 99, 89, 91, 95, 90]}
r4 = {"name": "马尔福", "score": [100, 85, 90]}
tb = [r1, r2, r3, r4]
# 求每个人的总成绩
for i in range(len(tb)):
    sum = 0
    for j in range(len(tb[i].get("score"))):
        sum += tb[i].get("score")[j]
    print("{0}的总成绩为：{1}".format(tb[i].get("name"), sum))


