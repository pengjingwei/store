# 人员数据库:
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# ["曹操", "56", "男", "106", "IBM", 500, "50"],
# ["大乔", "19", "女", "230", "微软", 501, "60"],
# ["小乔", "19", "女", "210", "Oracle", 600, "60"],
# ["许褚", "45", "男", "230", "Tencent", 700, "10"]

r1 = {"name": "曹操", "age": 56, "sex": "男", "eid": 106, "dep": "IBM", "salary": 500, "dnum": 50}
r2 = {"name": "大乔", "age": 19, "sex": "女", "eid": 230, "dep": "微软", "salary": 501, "dnum": 60}
r3 = {"name": "小乔", "age": 19, "sex": "女", "eid": 210, "dep": "Oracle", "salary": 600, "dnum": 60}
r4 = {"name": "许诸", "age": 45, "sex": "男", "eid": 230, "dep": "Tencent", "salary": 700, "dnum": 10}
tb = [r1, r2, r3, r4]

# 将数据转换为字典方式（姓名作为键，其他作为值
dict = {
    "刘备": {"age": 56, "sex": "男", "eid": 106, "dep": "IBM", "salary": 500, "dnum": 50},
    "大乔": {"age": 19, "sex": "女", "eid": 230, "dep": "微软", "salary": 501, "dnum": 60},
    "小乔": {"age": 19, "sex": "女", "eid": 210, "dep": "Oracle", "salary": 600, "dnum": 60},
    "张飞": {"age": 45, "sex": "男", "eid": 230, "dep": "Tencent", "salary": 700, "dnum": 10}
}
for i in  range(len(dict)):
    print(dict.popitem())

# 1.统计每个人的平均薪资
salary = 0
for i in range(len(tb)):
    salary += tb[i].get("salary")
print("平均薪资为：{0:.2f}".format(salary/len(tb)))

# 2.统计每个人的平均年龄
age = 0
for i in range(len(tb)):
    age += tb[i].get("age")
print("平均年龄为：{0:.2f}".format(age/len(tb)))

# 3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
r5 = {"name": "刘备", "age": 45, "sex": "男", "eid": 220, "dep": "alibaba", "salary": 500, "dnum": 30}
tb.append(r5)
print("姓名 年龄 性别 编号 任职公司 薪资 部门编号")
for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("sex"),tb[i].get("eid"),tb[i].get("dep"),
          tb[i].get("salary"),tb[i].get("dnum"))

# 4.统计公司男女人数
male = female = 0
for i in range(len(tb)):
    if tb[i].get("sex") == "男":
        male += 1
    else:
        female +=1
print("男性人数为：{0}人，女性人数为：{1}人".format(male, female))

# 5.每个部门的人数
lt = []
for i in range(len(tb)):
    lt.append(tb[i].get("dnum"))
setL = set(lt)
for i in range(len(setL)):
    view = setL.pop()
    print("部门编号为{0}的部门有{1}人".format(view, lt.count(view)))