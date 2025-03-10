# Task 1 - Counting Down with Loops
start = int(input("Enter the starting number: "))

while start > 0:
    print(start, end = "", flush = True)
    start -= 1

print("\nBlast off! ")

# Task 2 - Multiplication Table with for Loops
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3 - Find the Factorial

num2 = int(input("Enter another number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num2} is {factorial}.")