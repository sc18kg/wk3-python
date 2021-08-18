import os

file = open("order.txt")
data = file.read()
print(data)

parent_dir = os.path.dirname(__file__)
filepath = os.path.join(parent_dir + "order.txt")

# r = open for reading
# w = open in write-only mode
# x = exclusive creation - if file doesnt exist
# a = open for file appending
# t = text mode
# b = binary format
# + = Updating - read and write

try:
    with open(filepath) as file:
        data = list(map(lambda x: x.strip("\n"), file.readlines()))
        print(data)
        data.method_doesnt_exist()
        print("The file has now been closed")
except FileNotFoundError as errmsg:
    print("Could not find the right file", errmsg)
    data = []
except IndexError as errmsg:
    print(f"{file} is currently empty!", errmsg)
finally:
    print("This will happen if there is or isnt an error")

data = file.readlines()
line_1 = data[0].strip('\n')
line_2 = data[1].strip('\n')

for entry in data:
   clean_data = clean_data.append(entry.strip('\n'))
print(clean_data)

#Lambda

add = (lambda n1, n2: n1 + n2)
print(add(2, 4))

def double(n):
    return n * 2

numb = [1, 2, 3, 4, 5]

new_numb = map(double, numb)
print(new_numb)
print(list(new_numb))

new_numb = list(map(lambda n: (n * 2), numb))
print(new_numb)

savings = [234.00, 555.00, 674.00, 68.00]
new_savings = list(map(lambda n: n + (n * 0.1), savings))

def is_even(n):
    return n % 2 == 0


print(list(filter(lambda x: x % 2 == 0, numb)))




file.close()