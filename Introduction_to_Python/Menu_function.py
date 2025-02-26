import turtle

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fractal_pattern(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        fractal_pattern(branch_length - 15, t)
        t.left(40)
        fractal_pattern(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)


print("Welcome to the Recurisve Artistry Program!")
while True:
    print("\nChoose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Draw a Recurisve Fractal 4. Exit ")
    choice = input()
    if choice == "1":
        num = input("Enter a number to find its factorial: ")
        if num.isdigit():
            num = int(num)
            print(f"The factorial of {num} is {factorial(num)}")
        else:
            print("Please enter a valid positive integer")

    elif choice == "2":
        num = input("Enter the position of the Fibonacci number: ")
        if num.isdigit():
            num = int(num)
            print(f"The {num}th Fibonacci number is {fibonacci(num)}")
        else:
            print("Please enter a valid positive integer")

    elif choice == "3":
        print("Drawing a recursive fractal tree... (Close window to continue)")
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.color("green")
        t.speed(0)
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        fractal_pattern(100, t)
        screen.mainloop()
    
    elif choice == "4":
        print("Exiting program. Thank you for participating")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4")
