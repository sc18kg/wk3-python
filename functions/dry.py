# Dont
# Repeat
# Yourself

#Functions

def print_something(word1, word2): # snakecase
    print("Print")
    print(word1)
    print(word2)
    return 

# print_something("dog", "bark")
returned_numb = []

def add_plus1(int1: int, int2: int): # can use type hints which tell user what is expected
    a = int1 + int2 + 1
 #   returned_numb.append(a)  # dont change and return 
    return a

print(add_plus1(10,5))
x = add_plus1(10, 10)
print(x)

print(returned_numb)
