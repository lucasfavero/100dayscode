from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    client_option = input(f"What would you like? {menu.get_items()}?: ").lower()

    if client_option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(client_option)
        print(f"You choose: {item.name.capitalize()}. Price: $ {item.cost}")
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
