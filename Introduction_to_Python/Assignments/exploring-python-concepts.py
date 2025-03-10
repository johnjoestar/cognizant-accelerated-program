# Task 1 - Variables: Your First Python Intro
name = "John"
age = 23
height = 5.11

print (f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")

# Task 2 - Operators: Playing with Numbers
num1 = 12
num2 = 2

# Performing math
print(f"The sum of {num1} and {num2} is {num1 + num2}") # addition
print(f"The difference between {num1} and {num2} is {num1 - num2}") # subtraction
print(f"The product of {num1} and {num2} is {num1 * num2}") # multiplication
print(f"The quotient when {num1} is divided by {num2} is {num1/num2:.2f}") # division with correct format

# Task 3 - Conditional Statements: The Number Checker
num = float(input("Enter a number: "))

# checking for positive, negative, or zero
if num > 0:
    print("This number is a positive. Awesome!")

elif num < 0: 
    print("This number is negative. Better luck next time!")

else:
    print("Zero it is. A perfect balance!")