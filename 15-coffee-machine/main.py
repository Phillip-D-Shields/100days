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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """verifies there is enough of each ingredient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}!")
            return False
    return True


def process_coins():
    """returns total amount of coins inserted"""
    print("please insert coins: ")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickels: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_successful(amount_received, drink_cost):
    """returns true when payment is accepted, false when money_received is insufficient"""
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Your change is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money!")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕☕☕☕ here is your {drink_name} ☕☕☕☕!")


is_on = True

while is_on:
    choice = input("what would you like? \nespresso: 1.50 \nlatte: 2.50 \ncappuccino: 3.00\n ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("The coffee machine has:")
        for resource in resources:
            print(f"{resources[resource]} of {resource}")
        print(f"with a current profit of: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


# TODO add a refill function to add ingredients to the machine
# TODO add a function to check money amount as its inserted
# TODO think of more ways to improve (return on april 12th)
# TODO add a function to check if any ingredients are empty and alert the user