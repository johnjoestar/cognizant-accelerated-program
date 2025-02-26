import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR,
                    format="%(asctime)s - ERROR: %(message)s")

def get_number(prompt):
    while True:
        try: 
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("ZeroDivisionError occurred: division by zero.")
        print("Oops! Division by zero is not allowed.")
        return None

def menu():
    while True:
        print("\n Welcome to the Error-Free Calculator!")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

        elif choice == "5":
            print("Goodbye!")
            break   

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

menu()