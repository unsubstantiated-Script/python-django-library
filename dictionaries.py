# A dictionary stores key-value pairs,
# where each unique key is an index which holds the value associated with it.

# empty_dict = {}  # Empty dictionary
# print(empty_dict)
#
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
#
# print(phone_book)

# A popular practice is to create an empty dictionary and add entries later.


# empty_dict = dict() #Empty Dictionary
# print(empty_dict)
#
# phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# print(phone_book)
#
# # Alternative approach
# phone_book = dict([('Batman', 468426),
#                    ('Cersei', 237734),
#                    ('Ghostbusters', 44678)])
# print(phone_book)

# Accessing Values
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book["Cersei"])
# print(phone_book.get("Ghostbusters"))

# Dictionary Operations
# We can add new entries in a dictionary by simply assigning a value to a key. Python automatically creates the entry.

# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)
#
# phone_book["Godzilla"] = 46394  # New entry
# print(phone_book)
#
# phone_book["Godzilla"] = 9000  # Updating entry
# print(phone_book)

# Removing Entries
# Destroying
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)
#
# del phone_book["Batman"]
# print(phone_book)

# Popping off to store in a variable
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)
#
# cersei = phone_book.pop("Cersei")
# print(phone_book)
# print(cersei)
#
# # Removes and returns the last inserted pair, as a tuple
# # In Python versions before 3.7, popitem() removes and returns the random item
# lastAdded = phone_book.popitem()
# print(lastAdded)

# Length of a dictionary
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(len(phone_book))

# Checking if a key exists
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print("Batman" in phone_book)
# print("Godzilla" in phone_book)

# Copying bits from one dictionary to another in a sort of merge
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
#
# second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
#
# # Add secondphone_book to phone_book
# phone_book.update(second_phone_book)
# print(phone_book)

# Dictionaries also have comprehensions like lists
# houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
# new_houses = {n**2: house + "!" for (n, house) in houses.items()}
# print(houses)
# print(new_houses)
