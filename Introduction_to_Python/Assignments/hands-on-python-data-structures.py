# Task 1 - Working with Lists
fruits = ['apple', 'strawberry', 'tangerine', 'mango', 'watermelon']
print("Original list:", fruits)

fruits.append('grape')
print("After adding a fruit:", fruits)

fruits.remove('mango')
print("After removing a fruit:", fruits)

reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)

# Task 2 - Exploring Dictionaries
dont_dox_me = {
    "name": "John",
    "age": 23,
    "city": "Aubrey"
}

dont_dox_me["favorite color"] = "Red"

dont_dox_me["city"] = "Dallas"

print("Keys:", ", ".join(dont_dox_me.keys()))
print("Values:", ", ".join(str(value) for value in dont_dox_me.values()))

# Task 3 - Using Tuples
favorites = ('Avengers: Endgame', 'Cookie', 'Lord of the Mysteries')
print("Favorite things:", favorites)
try: 
    favorites[0] = 'Spirited Away'
except TypeError:
    print("Oops! Tuples cannot be changed.")

print("Length of tuple:", len(favorites))