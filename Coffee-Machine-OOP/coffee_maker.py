class CoffeeMaker:
    
    def __init__(self):
        self.resources = {
            "cream": 300,
            "milk": 200,
            "latte": 100,
        }

    def report(self):
        
        print(f"cream: {self.resources['cream']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"latte: {self.resources['latte']}g")

    def is_resource_sufficient(self, drink):
       
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
       
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
