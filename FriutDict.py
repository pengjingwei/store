# 用水果名称做key，金额做value，创建一个字典
# ‘苹果’：12.3，  # 水果和单价
# ‘草莓’：4.5，
# ‘香蕉’：6.3，
# ‘葡萄’：5.8，
# ‘橘子’：6.4，
# ‘樱桃’：15.8

friut = {"苹果": 32.8, "香蕉": 22, "葡萄": 15.5}
friuts = {
    "苹果": 12.3,
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
    }
}

info["小明"]["money"] = info["小明"]["fruits"]["苹果"] * friuts["苹果"] +\
    info["小明"]["fruits"]["草莓"] * friuts["草莓"] +\
    info["小明"]["fruits"]["香蕉"] * friuts["香蕉"]

# print(info["小明"]["fruits"].get("苹果") * friuts.get("苹果"))

info["小刚"]["money"] = info["小刚"]["fruits"]["葡萄"] * friuts["葡萄"] +\
    info["小刚"]["fruits"]["橘子"] * friuts["橘子"] +\
    info["小刚"]["fruits"]["樱桃"] * friuts["樱桃"]

print(info.items())
# print(info["小明"]["money"])
# print(info["小刚"]["money"])


