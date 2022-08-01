import machine_data


def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > machine_data.resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        return True


def count_coins():
    print("Please insert coins.")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.1
    total += int(input("Nickles: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total


def enough_coins(money_received, drink_price):
    if money_in >= drink_price:
        change = round(money_received - drink_price, 2)
        print(f"Here is your change: ${change}")
        machine_data.profit += drink_price
        return True
    else:
        print("Sorry, that's not enough money - money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        machine_data.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


machine_on = True
while machine_on:
    order = input("What coffee would you like to have? (espresso, latte, cappuccino): ")
    if order == "off":
        machine_on = False
    elif order == "report":
        print(f"Water: {machine_data.resources['water']}ml")
        print(f"Milk: {machine_data.resources['milk']}ml")
        print(f"Coffee: {machine_data.resources['coffee']}g")
        print(f"Money: ${machine_data.profit}")
    else:
        drink = machine_data.MENU[order]
        if check_resources(drink["ingredients"]):
            money_in = count_coins()
            if enough_coins(money_in, drink["cost"]):
                make_coffee(order, drink["ingredients"])
