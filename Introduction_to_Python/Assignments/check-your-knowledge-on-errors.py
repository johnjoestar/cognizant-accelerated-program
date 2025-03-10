# Task 1 - Understanding Python Exceptions
def division_100():
    while True:
        try:
            num = int(input("Enter a number:"))
            result = 100 / num
            print(f"100 divided by {num} is {result}.")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

division_100()

# Task 2 - Types of Exceptions
def exception_handler():
    try:
        test_list = [1, 2, 3]
        print(test_list[6])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    try:
        test_dict = {"name": "John"}
        print(test_dict["age"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    try:
        test_string = "hello" + 6
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

exception_handler()

# Task 3 - Using try...except...else...finally
def division_handling():
    try: 
        dividend = float(input("Enter the first number: "))
        divisor = float(input("Enter the second number: "))
        quotient = dividend / divisor
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")
    else:
        print(f"The result is {quotient}.")
    finally:
        print("This block always executes.")

division_handling()