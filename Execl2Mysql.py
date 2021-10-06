# 把excel中的数据存在一张表中
import xlrd
import DBUtils

wb = xlrd.open_workbook(filename=r"C:\Users\gamer\Desktop\python学习资料\day09【xlrd】\任务\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
# sheet = wb.sheet_by_name("5月")
sheets = wb.sheet_names()
for i in range(len(sheets)):
    sheet = wb.sheet_by_name(sheets[i])
    rows = sheet.nrows
    for j in range(rows):
        # print(sheet.row_values(j))
        if j == 0:
            sql = "create table %s月 (日期 varchar(50) primary key, 服装名称 varchar(50), 单件价格 double(20,2), 本月库存数量 int(20), 每日销售量 int(50))"
            param = [i+1]
            DBUtils.updata(sql, param)
        # 如果数据库已经存在了相关数据会报错，因为key primary已经存在
        else:
            sql = "insert into %s月 values (%s,%s,%s,%s,%s)"
            param = [i+1]
            param.extend(sheet.row_values(j))
            DBUtils.updata(sql, param)

