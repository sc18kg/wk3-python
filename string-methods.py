whitespace = "Here is a string with space     "
print(whitespace)
print(whitespace.strip()) # methods always follow the .function 
print(whitespace.find("string")) # finds the fist instance of the input in quote
print(whitespace.count("s")) # counts how many times it appears in string
print(whitespace.strip().count(" ")) # finds how many times a space appears before and after - you can chain methods

char = "HeLlO ThErE"
print(char.upper())
print(char.replace("E", "AAAA"))

name = "Kieron"
age = 24
height = "6'1"
number = 10.22345555
print(f"{name} is {age} years old and is {height}.")
print(f"{number} to 2dp is {number:.2f} and {number:.4f} is to 4dp")

score = 20
max_score = 24

print(f"You scored {score/max_score:.2%} ") #two decimal place percentage