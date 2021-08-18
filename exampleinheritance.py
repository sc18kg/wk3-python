
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

r = Rectangle(10, 20)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)  #Super refers to the init of the parent class so needs 2 params

s = Square(5)


print(s.get_area())
print(r.get_area())