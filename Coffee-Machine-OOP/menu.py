class MenuItem:
   
    def __init__(self, name, cream, milk, latte, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "cream": cream,
            "milk": milk,
            "latte": latte
        }


class Menu:
   
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cream=125, milk=100, latte=150, cost=2.5),
            MenuItem(name="espresso", cream=75, milk=60, latte=100, cost=1.5),
            MenuItem(name="cappuccino", cream=125, milk=100, latte =150, cost=3),
        ]

    def get_items(self):
       
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
       
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
