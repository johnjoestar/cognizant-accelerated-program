inventory = {
        "apple": (10, 2.5),
        "banana": (20, 1.2)
    }

def inventory_management():
    print("\nCurrent inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: {price:.2f}")
    print(f"Total value of inventory: ${calculate_total_value():.2f}")

def add_item(item, quantity, price):
    if item in inventory:
            print(f"{item} already exists! Use update option isntead.")
    else:
        inventory[item] = (quantity, price)
        print(f"Added {item} to inventory")

def remove_item(item):
    if item in inventory:
        del inventory[item]
        print(f"Removed {item} from inventory.")
    else:
        print(f"{item} not found in inventory.")

def update_item(item, quantity=None, price=None):
    if item in inventory:
        old_quantity, old_price = inventory[item]
        new_quantity = quantity if quantity is not None else old_quantity
        new_price = price if price is not None else old_price
        inventory[item] = (new_quantity, new_price)
        print(f"Update {item}: Quantity = {new_quantity}, Price = ${new_price:.2f}")
    else:
        print(f"{item} not found in inventory.")

def calculate_total_value():
    return sum(quantity * price for quantity, price in inventory.values())

print("Welcome to the Inventory Manager!")
while True:
    inventory_management()
    print("\nOptions: [1] Add Item [2] Remove Item [3] Update Item [4] Exit ")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter item name: ").lower()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_item(item, quantity, price)
    elif choice == "2":
        item = input("Enter item name to remove: ").lower()
        remove_item(item)
    elif choice == "3":
        item = input("Enter item name to update: ").lower()
        if item in inventory:
            quantity = input("Enter new quantity (press Enter to skip): ")
            price = input("Enter new price (press Enter to skip): ")
            update_item(item, int(quantity) if quantity else None, float(price) if price else None)
        else:
            print(f"{item} not found in inventory.")
    elif choice == "4":
        print("Exiting Inventory Manager...")
        break
    else:
        print("Invalid option. Please try again.")