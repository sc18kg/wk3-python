# Iterator

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if (num % 2) == 0:
        print(f"variable 'num' is now: {num}")
        print(num * 2, num + 10)

print("End")

# Nested lists
nested_list = [[1, 2, 3], [4, 5], [6]]
for x in nested_list:
    print(x)
    for num in x:
        print(num)