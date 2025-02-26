def password_checker(user_password):
    password_strength_meter = 0
    errors = []

    if len(user_password) < 8:
        errors.append("at least 8 characters long")
    else:
        password_strength_meter += 2

    if any(char.isupper() for char in user_password):
        password_strength_meter += 2
    else: 
        errors.append("one uppercase letter")

    if any(char.islower() for char in user_password):
        password_strength_meter += 2
    else: 
        errors.append("one lowercase letter")

    special_characters = "!@#$%&*()_+"
    if any(char in special_characters for char in user_password):
        password_strength_meter += 2
    else:
        errors.append("one special character")

    if errors:
        print(f"Your password needs {', '.join(errors)}.")

    if password_strength_meter == 8:
        print("Your password is strong!")
    elif password_strength_meter >= 6:
        print("Your password is Medium! Consider making it stronger.")
    else:
        print("Your password is Weak! Improve security by adding more security measures.")


user_password = input("Enter a password: ")
password_checker(user_password)