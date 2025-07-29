""" creating a dictionary called Menu to store all the items required
for a coffee .This coffee machine only has 3 coffee's which espresso, latte, cappuccino
and there ingredients.
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# created a resources dictionary to store the amount of water,milk, coffee data. 
resources = {
    "water": 1400,
    "milk": 900,
    "coffee": 500,
}
#
money = 0
profit_made =0
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def resources_sufficient(order_ingredients):
        for item in order_ingredients:
            if resources[item] < order_ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
def payment():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit_made
        profit_made += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


coffee_machine_is_on = True

while coffee_machine_is_on:

    user_choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        coffee_machine_is_on = False
    elif user_choice == "report":
       report()
    else:
        drink = MENU[user_choice]
        if resources_sufficient(drink["ingredients"]):
            print(f"{user_choice} is : ${drink['cost']}")
            payments_made = payment()
            if is_transaction_successful(payments_made, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
