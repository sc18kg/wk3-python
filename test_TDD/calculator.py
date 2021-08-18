import math

class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

class SciCalc(Calc):
    def find_swrt(self, numb):
        if numb:
            return math.sqrt(numb)
        else:
            return None


    def find_ceil(self, numb):
        return math.ceil(numb)


        



