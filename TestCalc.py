# unittest自动化测试框架

from unittest import TestCase
import calculator


class TestCalc(TestCase):
    def testAdd1(self):
        a = 1
        b = 2
        s = 3
        calc = calculator.Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd2(self):
        a = -5
        b = -2
        s = -7
        calc = calculator.Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd3(self):
        a = -6
        b = 2
        s = -4
        calc = calculator.Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd4(self):
        a = 9
        b = -3
        s = 6
        calc = calculator.Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd5(self):
        a = 99999999999999999999999999
        b = 1
        s = 100000000000000000000000000
        calc = calculator.Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)
