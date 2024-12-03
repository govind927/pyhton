# Set Initialization
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding an element
my_set.add(6)
print("\nAfter Adding an Element:", my_set)

# Removing an element using remove() (raises error if element not found)
my_set.remove(3)
print("After Removing Element 3:", my_set)

# Removing an element using discard() (does not raise error if element not found)
my_set.discard(7)  # No error even if 7 is not in the set
print("After Trying to Discard Non-Existent Element 7:", my_set)

# Removing an arbitrary element using pop()
removed_element = my_set.pop()
print("After Popping an Element:", my_set)
print("Popped Element:", removed_element)

# Clearing the set
my_set.clear()
print("\nAfter Clearing the Set:", my_set)

# Reinitializing for further operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print("\nUnion of Set A and Set B:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference of Set A and Set B:", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of Set A and Set B:", symmetric_difference_set)

# Checking Subset and Superset
print("\nIs Set A a Subset of Set B?", set_a.issubset(set_b))
print("Is Set A a Superset of Set B?", set_a.issuperset(set_b))

# Checking Disjoint
print("Are Set A and Set B Disjoint?", set_a.isdisjoint(set_b))

# Iterating through a set
print("\nIterating through Set A:")
for element in set_a:
    print(element)

# Copying a set
copied_set = set_a.copy()
print("\nCopied Set A:", copied_set)

# Using update to add multiple elements
set_a.update({6, 7})
print("\nAfter Updating Set A with {6, 7}:", set_a)
