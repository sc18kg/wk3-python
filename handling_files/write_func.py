import os


file = open("drinks_menu.txt")
menu = list(map(lambda x: x.strip("\n"), file.readlines()))

parent_dir = os.path.dirname(__file__)
filepath = os.path.join(parent_dir + "drinks_menu.txt")


def order(drink_order, menu):
    try:
        with open(filepath, "r") as menu:
            if drink_order in menu:
                print(f"Your order of {order} can be completed")
            
    except:
        print("Drink isnt on Menu")
        
print(menu)
order("Pornstar Martini", menu)
