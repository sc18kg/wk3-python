def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


def calc (num1, sign, num2):

    if "+" in sign:
       return add(num1, num2)

    if "-" in sign:
        return sub(num1, num2)

    if "/" in sign:
        return div(num1, num2)

    if "*" in sign:
        return mult(num1, num2)

num1 = int(input("Please enter your first digit\n"))
sign = input("Please specify the calculation you require out of + , - , / , * :\n")

num2 =  int(input("Please enter your second digit: \n"))
print(f"Calculation is {num1} {sign} {num2} =")

print(calc(num1, sign, num2))