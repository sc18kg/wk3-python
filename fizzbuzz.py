numb = range(101)

for numb in range(1, 101):
    if (numb %3 == 0) and (numb %5 == 0):
        print(f"({numb}) - FizzBuzz")
    elif (numb % 3 == 0):
        print(f"({numb}) - Fizz")
    elif (numb % 5 == 0):
        print(f"({numb}) - Buzz")
    else:
        print(numb)