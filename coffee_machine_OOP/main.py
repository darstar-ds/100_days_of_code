from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


profit = 0

# coffee_items = MenuItem()
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    coffee_types = coffee_menu.get_items()
    choice = input(f"​What would you like? ({coffee_types}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        # print(drink)
        # print(choice)
        # print(type(drink))
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(coffee_menu.find_drink(choice).cost):
                coffee_machine.make_coffee(drink)








