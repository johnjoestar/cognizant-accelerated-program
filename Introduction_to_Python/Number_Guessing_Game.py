import random
number_to_guess = random.randint(1,100)

attempts = 0

while attempts < 11:
    guess_input = int(input("Guess the number (between 1 and 100): "))
    if guess_input > number_to_guess:
        print(str(guess_input) + " Too high! Try again.")
        attempts += 1
    elif guess_input < number_to_guess:
        print(str(guess_input) + " Too low! Try again.")
        attempts += 1
    elif guess_input == number_to_guess:
        print(str(guess_input) + " Congratulations! You guessed it in " + str(attempts) + " attempts!")
    else:
        print("Game Over! Better luck next time!")