'''
Author name: Jeremiah
Code description: Practice/favorite fruit is used for checking how much
fruit is left after the user places an order
Last Updated Date: 6/1/19
'''


def check_fruit_quantity(fruit_info, item_qty):
    """
    Check the quantity of a specific fruit after an order is placed.

    Parameters:
    - fruit_info: Dictionary containing information about the fruit.
    - item_qty: Quantity of the fruit ordered.

    Returns:
    - The remaining quantity of the fruit.
    """
    qty_left = fruit_info['quantity'] - item_qty
    return max(qty_left, 0)


def main():
    fruit_inventory = {
        'mango': {'quantity': 5, 'price': 2.99},
        'orange': {'quantity': 6, 'price': 1.99},
        'kiwi': {'quantity': 10, 'price': 0.99},
        'apple': {'quantity': 3, 'price': 1.49}
    }

    while True:
        print("Available fruits:")
        for fruit, info in fruit_inventory.items():
            print(f"{fruit.capitalize()}: Quantity: {info['quantity']}, Price: ${info['price']}")

        fav_fruit = input("Enter a fruit (or type 'quit' to exit): ").lower()

        if fav_fruit == 'quit':
            print("Exiting the program. Goodbye!")
            break

        if fav_fruit not in fruit_inventory:
            print("Sorry, item not found.")
        else:
            try:
                item_qty = int(input("Enter qty: "))
                if item_qty < 0:
                    print("Invalid quantity. Please enter a non-negative number.")
                else:
                    updated_qty = check_fruit_quantity(fruit_inventory[fav_fruit], item_qty)
                    fruit_inventory[fav_fruit]['quantity'] = updated_qty
                    print(f"Qty of {fav_fruit} left: {updated_qty}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("\n")
    for _ in range(20):
        print("__", end="")


if __name__ == "__main__":
    main()
