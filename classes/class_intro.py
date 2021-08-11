class Dog:
    animal_type = "canine"

    def bark(self):
        return (f"Woof! I am {self.name}")

 # Initialising
    def __init__(self, name, colour): # only has two arguments cause self doesnt count
        self.name = name
        self.colour = colour
        self.legs = 4
        self.animal_type = "canine"
        self.bark()   # everything in class is provided at once so call call method in method
#Instantiation

fido = Dog('Fido', 'Black')
lassie = Dog('Lassie', 'Brown')

#fido.legs = 2
#print(fido.animal_type)
#print(fido.colour)

class Cart:

    def __init__(self):
        self.items = []

    def add_shopping(self, new_item):
        self.items.append(new_item)

    def view_shopping(self):
        for product in self.items:
            print(f"Item: {product.name}\nBrand:{product.brand}\nPrice:£{product.price}")
    
    def get_total(self):
        total = 0
        for product in self.items:  # The underscore hides the contents telling the user to use methods double youre not allowed to touch
            total += product.price
        return f"Total Cost of Shopping: £{total}"



class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

sc = Cart()
sc.add_shopping(Product("Bread", 1.09, "Morrisons"))
sc.add_shopping(Product("Chicken", 4.09, "Morrisons"))
sc.view_shopping()
print(sc.get_total())