# Task 1 - String Slicing and Indexing
text = "Python is amazing!"

first_characters = text[:6]
amazing_character = text[10:17]
reverse_text = text[::-1]

print("First word:", first_characters)
print("Amazing part:", amazing_character)
print("Reversed String:", reverse_text)

# Task 2 - String Methods
text2 = " hello, python world! "

strip_text = text2.strip()
capitalize_text = strip_text.capitalize()
replace_text = strip_text.replace("world", "universe")
upper_text = strip_text.upper()

print(text2)
print(strip_text)
print(capitalize_text)
print(replace_text)
print(upper_text)

# Task 3 - Check for Palindromes
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")

else:
    print(f"No, '{word}' is not a palindrome.")