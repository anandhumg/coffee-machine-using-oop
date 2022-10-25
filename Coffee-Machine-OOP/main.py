from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    machine_on = True
    while machine_on:
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif coffee_maker.is_resource_sufficient(menu.find_drink(user_choice)):
            menu_choice = menu.find_drink(user_choice)
            money_machine.make_payment(menu_choice.cost)
            coffee_maker.make_coffee(menu_choice)


if __name__ == "__main__":
    main()
