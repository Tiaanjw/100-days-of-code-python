from coffee_machine_data import MENU, resources
import os
clear = lambda: os.system('clear')

def generate_report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${resources['money']}")

def check_resources(selection):
  if resources["water"] <= MENU[selection]["ingredients"]["water"]:
    return "Sorry there is not enough water"
  elif resources["milk"] <= MENU[selection]["ingredients"]["milk"]:
    return "Sorry there is not enough milk"
  elif resources["coffee"] <= MENU[selection]["ingredients"]["coffee"]:
    return "Sorry there is not enough milk"
  else:
    return True
  
def take_money(selection):
  selection_price = MENU[selection]["cost"]
  print(f"Please insert coins, price ${selection_price}")
  
  quarters = int(input("How many quarters? ($0.25): "))
  dimes = int(input("How many dimes? ($0.10): "))
  nickels = int(input("How many nickels? ($0.05): "))
  pennies = int(input("How many pennies? ($0.01): "))

  total = float("{:.2f}".format((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)))

  if total >= selection_price:
    refund_amount = total - selection_price
    print(f"Amount received ${total}, refund amount ${refund_amount}")
    resources["money"] += selection_price
    return True
  
  else:
    print(f"That is not enough, the price is ${selection_price}, refunding ${total}")
    return False
  
def make_coffee(selection):
  resources["water"] -= MENU[selection]["ingredients"]["water"]
  resources["milk"] -= MENU[selection]["ingredients"]["milk"]
  resources["coffee"] -= MENU[selection]["ingredients"]["coffee"]
  return True

def queue_coffee(selection):
  print(f"Making {selection}...")
  
  resources_available = check_resources(selection)
  if resources_available != True:
    print(resources_available)
    return
  
  success = take_money(selection)
  if not success:
    return
  
  make_coffee(selection)
  
  print(f"Here is your {selection}, please enjoy!")


while True:
  selection = input("What would you like? (espresso/latte/cappuccino): ")

  if selection == "report":
    generate_report()
  elif selection == "exit":
    exit()
  elif selection in MENU:
    queue_coffee(selection)
  else:
    print("Invalid selection, please try again.")
