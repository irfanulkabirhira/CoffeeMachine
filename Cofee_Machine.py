# Constants and global dictionaries

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

# Track total profit from sales
profit = 0.0

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resources_sufficient(order_ingredients):
    """
    Checks machine resources against the required ingredients for the order.
    
    Returns:
        bool: True if the order can be made; False if resources are insufficient
              for at least one ingredient.
    """
    for item, required_amount in order_ingredients.items():
        if required_amount > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Prompts the user for the number of each coin type inserted.
    
    Returns:
        float: The total dollar amount based on the coins inserted.
    """
    print("Please insert coins.")
    total = 0.0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? "))   * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Verifies if the inserted money is sufficient to pay for the drink.

    Args:
        money_received (float): The total money inserted by the user.
        drink_cost (float): The cost of the chosen drink.

    Returns:
        bool: True if there's enough money; False otherwise.
              If True and there's excess, it returns the user’s change.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from the machine resources
    and outputs a success message.

    Args:
        drink_name (str): The name of the drink (e.g., 'latte').
        order_ingredients (dict): Ingredient amounts used by that drink.
    """
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕. Enjoy!")


def print_report():
    """
    Prints the current resource levels and total profit so far.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def coffee_machine_loop():
    """
    Main loop that runs the coffee machine logic.
    User can type coffee name, 'report', or 'off'.
    """
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            # Turn off the coffee machine
            is_on = False

        elif choice == "report":
            # Display current resources & profit
            print_report()

        elif choice in MENU:
            # Attempt to make one of the known drinks
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            # Invalid user input
            print("Invalid option. Please choose espresso, latte, cappuccino, 'report', or 'off'.")


# If desired, you can automatically run the machine loop here:
# coffee_machine_loop()
