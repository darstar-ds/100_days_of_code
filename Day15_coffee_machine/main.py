from dict import MENU, resources
import os


print(MENU)

print(resources)

def calculate_coins(quarters_no, dimes_no, nikels_no, pennies_no):
    #Takes the number of coins and returns the sum
    return int(0.25*quarters_no + 0.1*dimes_no + 0.05*nikels_no + 0.01*pennies_no)


def verify_resources(user_wish, water, milk, coffee):
    # print(MENU[user_wish]["ingredients"]["water"])  
    try:
        drink_milk = MENU[user_wish]["ingredients"]["milk"]
    except KeyError:
        drink_milk = 0
    # print(f"Drink_milk = {drink_milk}")
    if MENU[user_wish]["ingredients"]["water"]>water:
        return print("Sorry, there is not enough water.")
    elif drink_milk>milk:
        return print("Sorry, there is not enough milk.")
    elif MENU[user_wish]["ingredients"]["coffee"]>coffee:
        return print("Sorry, there is not enough coffee.")
    else:
        return True    

def do_the_drink(ins_money, money, user_wish, water, milk, coffee, drink_water, drink_milk, drink_coffee):
    money += MENU[user_wish]["cost"]
    water -= drink_water
    milk -= drink_milk
    coffee -= drink_coffee
    return money, water, milk, coffee

os.system("cls")
is_on = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
# print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")

while is_on:
    user_wish = input("What would you like (espresso/latte/cappuccino): ")
    while user_wish not in ("espresso", "latte", "cappuccino", "off", "report"):
        user_wish = input("What would you like (espresso/latte/cappuccino): ")


    if user_wish == "off":
        # if the user insert "off" the machine is off
        is_on = False
    elif user_wish == "report":
        # if the user wants the report print amount of ingredients
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
    else:
        try:
            drink_milk = MENU[user_wish]["ingredients"]["milk"]
        except KeyError:
            drink_milk = 0
        try:
            drink_water = MENU[user_wish]["ingredients"]["water"]
        except KeyError:
            drink_water = 0
        try:
            drink_coffee = MENU[user_wish]["ingredients"]["coffee"]
        except KeyError:
            drink_coffee = 0

        enough_resources = verify_resources(user_wish, water, milk, coffee)
        if enough_resources:
            print("Please insert coins.")
            quarters_no = int(input("how many quarters?: "))
            dimes_no = int(input("how many dimes?: "))
            nickels_no = int(input("how many nickels?: "))
            pennies_no = int(input("how many pennies?: "))
            ins_money = calculate_coins(quarters_no, dimes_no, nickels_no, pennies_no)
            if ins_money >= MENU[user_wish]["cost"]:
                change = ins_money - MENU[user_wish]["cost"]
                print(f"Here is ${change} in change.")
                money, water, milk, coffee = do_the_drink(ins_money, money, user_wish, water, milk, coffee, drink_water, drink_milk, drink_coffee)
                print(f"Here is your {user_wish}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
