# 任务1：
#     2020年全年的销售统计分析
# 全年的销售总额
# 每件衣服的销售（件数）占比:羽绒服、牛仔裤、风衣、皮衣、皮草、t血、马甲、小西衬衫、卫衣、棉衣、铅笔裤
# 每件衣服的月销售占比
# 每件衣服的销售额占比
# 最畅销的衣服是那种
# 每个季度最畅销的衣服
# 全年销量最低的衣服
# 任务2：
#     写个算法，把excel中的数据存在一张表中。
#     写个算法，把三国集团的数据，存在Excel表里。

import xlrd

wb = xlrd.open_workbook(filename=r"C:\Users\gamer\Desktop\python学习资料\day09【xlrd】\任务\2020年每个月的销售情况.xlsx",
                        encoding_override=True)

money = sale = max = 0
min = 100000
qmax = [0, 0, 0, 0]
qmaxN = ["", "", "", ""]
maxN = minN = ""
monthsale = {}
mcount = {}
msale = {}
qsale = {}
sheets = wb.sheet_names()  # 获取工作簿中所有表的名称

for i in range(len(sheets)):
    sheet = wb.sheet_by_name(sheets[i])
    rows = sheet.nrows
    for j in range(1, rows):
        t = sheet.row_values(j)[1]
        if t in monthsale:
            pass
        else:
            monthsale[t] = 0
        if t in mcount:
            pass
        else:
            mcount[t] = 0
        if t in msale:
            pass
        else:
            msale[t] = 0
        if t in qsale:
            pass
        else:
            m = {t: [0, 0, 0, 0]}
            qsale.update(m)
for i in range(len(sheets)):
    sheet = wb.sheet_by_name(sheets[i])  # 从工作簿取出每一张表
    rows = sheet.nrows
    count = 0
    for key in mcount:
        mcount[key] = 0
    for j in range(1, rows):
        money += sheet.row_values(j)[2] * sheet.row_values(j)[4]  # 计算全年的销售总额
        count += sheet.row_values(j)[4]  # 计算每月总销售量
    for j in range(1, rows):
        t = sheet.row_values(j)[1]
        monthsale[t] += sheet.row_values(j)[4]  # 每种衣服全年销量
        mcount[t] += sheet.row_values(j)[4] # 每种衣服每月销量
        msale[t] += sheet.row_values(j)[2] * sheet.row_values(j)[4]  # 每种衣服全年销售额
        # 计算每种衣服季度总销量
        if sheets[i] == "3月" or sheets[i] == "4月" or sheets[i] == "5月":
            qsale[t][0] += sheet.row_values(j)[4]
        if sheets[i] == "6月" or sheets[i] == "7月" or sheets[i] == "8月":
            qsale[t][1] += sheet.row_values(j)[4]
        if sheets[i] == "9月" or sheets[i] == "10月" or sheets[i] == "11月":
            qsale[t][2] += sheet.row_values(j)[4]
        if sheets[i] == "12月" or sheets[i] == "1月" or sheets[i] == "2月":
            qsale[t][3] += sheet.row_values(j)[4]
    for key in mcount:
        print("{0}在{1}月销售占比：{2:.2f}".format(key, i + 1, mcount[key] / count))
    sale += count  # 计算全年总销售量

for key in qsale:
    for i in range(4):
        if qsale[key][i] > qmax[i]:
            qmax[i] = qsale[key][i]
            qmaxN[i] = key
for i in range(4):
    print("第{0}季度最畅销的衣服是：{1}".format(i+1, qmaxN[i]))

for key in monthsale:
    if monthsale[key] > max:
        max = monthsale[key]
        maxN = key
    if monthsale[key] < min:
        min = monthsale[key]
        minN = key
    print("{0}全年销售占比：{1:.2f}".format(key, monthsale[key] / sale))
    print("{0}销售额占比：{1:.2f}".format(key, msale[key] / sale))
print("全年最畅销的衣服是{0}，销量最低的衣服是{1}".format(maxN, minN))
print("全年的销售总额:{0:.2f}".format(money))
