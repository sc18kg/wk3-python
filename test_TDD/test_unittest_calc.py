from calculator import Calc
from unittest import TestCase


class CalcTests(TestCase):
    calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(12,5), 17)  #firsttwo are the provided and last is the total
        self.assertEqual(self.calc.add(-5, -20), -25)

    def test_sub(self):
        self.assertEqual(self.calc.sub(12,5), 7) 
        self.assertEqual(self.calc.sub(2,5), -3) 

    def test_div(self):
        self.assertEqual(self.calc.div(20,5), 4) 
        self.assertEqual(self.calc.div(21,5), 4.2) 
    
    def test_multi(self):
        self.assertEqual(self.calc.multi(12,3), 36) 
        self.assertEqual(self.calc.multi(10,5.5), 55) 





















# python -m unittest - to run in console
# python -m pytest --cov 
