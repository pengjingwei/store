# 单例模式

class Singleton:
    __obj = None
    __flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if self.__flag:
            print("init...")
            self.name = name
            self.__flag = False


singleton = Singleton("张三")
single = Singleton("李四")
print(singleton.name)
print(single.name)
print(id(singleton))
print(id(single))
