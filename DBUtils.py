# 操作数据库工具类
import pymysql

host = "localhost"
user = "root"
password = "pjw9285851"
# database = "bank"
database = "cloth"


# def database(host, user, password, database):


def updata(sql, param):
    con = pymysql.Connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    con.commit()
    cursor.close()
    con.close()


def select(sql, param, model="all", size=1):
    con = pymysql.Connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if model == "all":
        return cursor.fetchall()
    elif model == "one":
        return cursor.fetchone()
    elif model == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()
