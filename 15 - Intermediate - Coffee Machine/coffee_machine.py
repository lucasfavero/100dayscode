MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_inside = 0.0


def validate_resources(option):
    if MENU[option]["ingredients"]["water"] > resources["water"]:
        print("Resource water isn't available, sorry. ")
        return False
    elif MENU[option]["ingredients"]["milk"] > resources["milk"]:
        print("Resource milk isn't available, sorry. ")
        return False
    elif MENU[option]["ingredients"]["coffee"] > resources["coffee"]:
        print("Resource coffee isn't available, sorry. ")
        return False
    else:
        return True


def transaction(coins, option):
    global coins_inside
    if coins >= MENU[option]["cost"]:
        print(f"Value inserted: ${coins:.2f}. {option.capitalize()} costs: ${MENU[option]['cost']}. Your change is: "
              f"${coins - MENU[option]['cost']:.2f}.")
        coins_inside += MENU[option]['cost']
        return True
    else:
        print(f"Value inserted: ${coins:.2f}. {option.capitalize()} costs: ${MENU[option]['cost']}. Refunding your "
              f"coins.")
        return False


def payment():
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total


def remove_resources(option):
    resources["water"] = resources["water"] - MENU[option]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[option]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[option]["ingredients"]["coffee"]
    return True


def report():
    print(f"Water:\t\t{resources['water']} \n"
          f"Milk:\t\t{resources['milk']} \n"
          f"Coffee:\t\t{resources['coffee']} \n"
          f"Coins:\t\t{coins_inside}")


def coffee_machine():
    while True:
        client_option = input("What would you like? Espresso, Latte or Cappuccino?. ").lower()
        if client_option == 'report':
            report()
        elif validate_resources(client_option):
            payed_coins = payment()
            if transaction(payed_coins, client_option):
                remove_resources(client_option)
                print(f"Here is your: {client_option.capitalize()}")


coffee_machine()
