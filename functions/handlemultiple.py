# Handling multiple arguments

def handle_multi(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


handle_multi(1, 2, 3)


def average(*multiargs):
    total = 0 # sum(multiargs)   cause its a tuple
    count = 0 # len(multiargs)   cause its a tuple
    for arg in multiargs:
        total += arg
        count += 1
    return total / count

print(average(12323, 345, 2345, 677, 234555, 4, 3733773737333))