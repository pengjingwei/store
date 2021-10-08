#  把三国集团的数据，存在Excel表里。
import xlwt
import DBUtils

sql = "select * from t_employees"
param = []
db = DBUtils.select(sql, param)
lt = []
# print(db)
wb = xlwt.Workbook()
st = wb.add_sheet("t_employees")
for t in db:
    L = list(t)
    lt.append(L)

for i in range(len(lt)):
    for j in range(len(lt[i])):
        st.write(i, j, lt[i][j])
wb.save("t_employees.xls")
