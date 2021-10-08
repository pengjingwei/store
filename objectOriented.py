# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体
class Cup:
    def __init__(self, high, volume, color, material):
        self.__high = high
        self.__volume = volume
        self.__color = color
        self.__material = material

    def storeLiquid(self):
        print("{0}材质的杯子能装{1}升的水".format(self.__material, self.__volume))


c = Cup(30, 0.5, "red", "钢")
c.storeLiquid()


# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class Computer:
    def __init__(self, screen, price, cpu, ram, hour):
        self.__screen = screen
        self.__price = price
        self.__cpu = cpu
        self.__ram = ram
        self.__hour = hour

    def type(self):
        print("电脑能打{0}小时的字".format(self.__hour))

    def play(self):
        print("用{0}的cpu，{1}的RAM玩游戏".format(self.__cpu, self.__ram))

    def watchVideo(self):
        print("在{0}英寸的屏幕上看视频".format(self.__screen))


computer = Computer(35, 15000, "intel core i9", "英伟达 GTX3090", 36)
computer.type()
computer.play()
computer.watchVideo()


# 定义了一个学生类：
# 属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
# 行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），
#         编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class Student:
    def __init__(self, sno, name, sex, age, high, weigh, score, address, phone):
        self.__sno = sno
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__high = high
        self.__weigh = weigh
        self.__score = score
        self.__address = address
        self.__phone = phone

    def getSno(self):
        return self.__sno

    def setSno(self, sno):
        self.__sno = sno

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSex(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age < 0 or age > 150:
            print("年龄输入错误")
        else:
            self.__age = age

    def getHigh(self):
        return self.__high

    def setHigh(self, high):
        if high < 0.8 or high > 2.6:
            print("身高非法")
        else:
            self.__high = high

    def getWeigh(self):
        return self.__weigh

    def setWeigh(self, weigh):
        if weigh < 50 or weigh > 300:
            print("体重非法")
        else:
            self.__weigh = weigh

    def getScore(self):
        return self.__score

    def setScore(self, score):
        if score < 0 or score > 100:
            print("分数非法")
        else:
            self.__score = score

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def study(self, hour):
        print("{0}已经学习了{1}小时".format(self.__name, hour))

    def play(self, gameName):
        print("{0}在玩{1}".format(self.__name, gameName))

    def programming(self, num):
        print("年龄{0}岁的{1}同学已经完成了{2}行代码".format(self.__age, self.__name, num))

    def sum(self, *a):
        sum = 0
        for i in a:
            sum += i
        return sum


s = Student("123456", "张三", "男", 18, 1.7, 140, 98, "中国", "1356423156")
s.play("APEX英雄")
print(s.sum(1, 2, 3))


# 车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
# 创建：法拉利，宝马，铃木，五菱，拖拉机对象
class Car:
    def __init__(self, model, wheels, color, tank):
        self.__model = model
        self.__wheels = wheels
        self.__color = color
        self.__tank = tank

    def run(self, function):
        print("{0}正在{1}".format(self.__model, function))


car = Car("宝马", 4, "白色", 3)
car.run("赛车")


# 猴子类：属性：类别，性别，身体颜色，体重。
# 行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class Monkey:
    def __init__(self, category, sex, color, weigh):
        self.__category = category
        self.__sex = sex
        self.__color = color
        self.__weigh = weigh

    def makeFire(self, material):
        print("{0}会用{1}造火".format(self.__category, material))

    def study(self, *a):
        print("{0}能学习{1}".format(self.__category, a))


monkey = Monkey("金丝猴", "男", "金色", 60)
monkey.study("说话", "唱歌", "跳舞")
monkey.makeFire("木头")
