from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

sage = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    items = menu.get_items()
    selection = input(f"What would you like? ({items}): ")

    if selection == "report":
        sage.report()
        money_machine.report()
        continue
    elif selection == "exit":
        exit()
  
    drink = menu.find_drink(selection)
    if not sage.is_resource_sufficient(drink):
        continue

    if not money_machine.make_payment(drink.cost):
        continue

    sage.make_coffee(drink)


