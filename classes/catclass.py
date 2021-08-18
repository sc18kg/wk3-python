class Cat:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old cat"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old cat"
        elif format_spec == "space dog":
            return f"{self.age * 20} space-dog years old"
        else:
            return self.__str__()

whiskers = Cat(6)
print(f"Whiskers is {whiskers}")
print(f"Whiskers is {whiskers:dog}")
print(f"Whiskers is {whiskers:space dog}")