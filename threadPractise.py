# 3个厨子造蛋挞，造的蛋挞放在一个能装500个蛋挞的盘子里，盘子装满，厨师等待三秒
# 有6个人，每人3000元，同时去购买盘子里的蛋挞，每个蛋挞2元，盘子为空等待3秒，直至钱用完

from threading import Thread
import time

plate = 0
# money = 3000


class Cooker(Thread):

    def run(self) -> None:
        global plate
        # global money
        # start = time.time()
        while True:
            if plate < 500:
                plate = plate + 1
                print("cooker造了一个蛋挞")
                # time.sleep(0.1)
            else:
                time.sleep(3)
                # end = time.time()
                # if end - start > 6:
                #     break
                # if money <= 0:
                #     break


class Person(Thread):
    money = 3000
    count = 0

    def run(self) -> None:
        global plate
        # global money
        while True:
            if self.money - 2 >= 0:
                if plate > 0:
                    self.money = self.money - 2
                    plate = plate - 1
                    self.count += 1
                    print("客人购买了一个蛋挞")
                    # time.sleep(0.1)
                else:
                    time.sleep(3)
            else:
                print("钱花完了,买了{0}个蛋挞".format(self.count))
                break


cooker1 = Cooker()
cooker2 = Cooker()
cooker3 = Cooker()

person1 = Person()
person2 = Person()
person3 = Person()
person4 = Person()
person5 = Person()
person6 = Person()

cooker1.start()
cooker2.start()
cooker3.start()

person1.start()
person2.start()
person3.start()
person4.start()
person5.start()
person6.start()
