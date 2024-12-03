# Dictionary Initialization
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "traveling", "painting"]
}

# Display the dictionary
print("Original Dictionary:", my_dict)

# Adding a key-value pair
my_dict["profession"] = "Engineer"
print("\nAfter Adding a Key-Value Pair:", my_dict)

# Updating a value
my_dict["age"] = 26
print("\nAfter Updating a Value:", my_dict)

# Accessing a value
print("\nAccessing 'name':", my_dict["name"])

# Using get() to access a value
print("Using get() to Access 'city':", my_dict.get("city"))

# Removing a key-value pair using pop()
removed_value = my_dict.pop("city")
print("\nAfter Removing 'city':", my_dict)
print("Removed Value:", removed_value)

# Removing the last key-value pair using popitem()
key, value = my_dict.popitem()
print("\nAfter Removing the Last Item:", my_dict)
print("Removed Item:", key, "->", value)

# Checking if a key exists
print("\nIs 'age' a key in the dictionary?", "age" in my_dict)

# Iterating through keys
print("\nKeys in the dictionary:")
for key in my_dict.keys():
    print(key)

# Iterating through values
print("\nValues in the dictionary:")
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
print("\nKey-Value Pairs in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Clearing all items in the dictionary
my_dict.clear()
print("\nAfter Clearing the Dictionary:", my_dict)

# Reinitializing the dictionary for further operations
my_dict = {"a": 1, "b": 2, "c": 3}

# Copying a dictionary
copied_dict = my_dict.copy()
print("\nCopied Dictionary:", copied_dict)

# Using fromkeys() to create a dictionary with default values
keys = ["x", "y", "z"]
default_dict = dict.fromkeys(keys, 0)
print("\nDictionary Created Using fromkeys():", default_dict)

# Using setdefault() to set a value for a key if it doesn't exist
default_value = my_dict.setdefault("d", 4)
print("\nAfter Using setdefault():", my_dict)
print("Default Value:", default_value)

# Merging dictionaries using update()
my_dict.update({"e": 5, "f": 6})
print("\nAfter Merging Dictionaries Using update():", my_dict)
