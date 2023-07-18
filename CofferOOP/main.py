from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# latte1 = MenuItem("Latte",300,200,100,2.5)
# latte2 = MenuItem("Latte",300,200,100,2.5)
# print(latte1.name)
# print(latte2.name)
# menu = Menu()
# print(menu.get_items())
# print(menu.find_drink("latte").name)


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on= True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
