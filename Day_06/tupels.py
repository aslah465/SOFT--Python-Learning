# Python Tuples Practice
# Topics:
# 1. Creating a Tuple
# 2. Tuple Length
# 3. Accessing Tuple Items
# 4. Slicing Tuples
# 5. Changing Tuples to Lists
# 6. Checking an Item in a Tuple
# 7. Joining Tuples
# 8. Deleting Tuples


# --------------------------------------------------
# 1. Creating a Tuple
# --------------------------------------------------

empty_tuple = ()
print("Empty tuple:", empty_tuple)

fruits = ("banana", "orange", "mango", "lemon")
print("Fruits tuple:", fruits)

single_item_tuple = ("apple",)
print("Single item tuple:", single_item_tuple)


# --------------------------------------------------
# 2. Tuple Length
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")
print("Number of fruits:", len(fruits))


# --------------------------------------------------
# 3. Accessing Tuple Items
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("Second last fruit:", fruits[-2])


# --------------------------------------------------
# 4. Slicing Tuples
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")

print("All fruits:", fruits[0:4])
print("Orange and mango:", fruits[1:3])
print("From orange to end:", fruits[1:])
print("Using negative slicing:", fruits[-3:-1])


# --------------------------------------------------
# 5. Changing Tuples to Lists
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")

fruits_list = list(fruits)
print("Tuple converted to list:", fruits_list)

fruits_list[0] = "apple"
print("Modified list:", fruits_list)

fruits = tuple(fruits_list)
print("List converted back to tuple:", fruits)


# --------------------------------------------------
# 6. Checking an Item in a Tuple
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")

print("Is banana in fruits?", "banana" in fruits)
print("Is apple in fruits?", "apple" in fruits)


# --------------------------------------------------
# 7. Joining Tuples
# --------------------------------------------------

fruits = ("banana", "orange", "mango")
vegetables = ("carrot", "potato", "onion")

food = fruits + vegetables

print("Joined tuple:", food)


# --------------------------------------------------
# 8. Deleting Tuples
# --------------------------------------------------

fruits = ("banana", "orange", "mango", "lemon")

print("Before deleting:", fruits)

del fruits

# Uncommenting the line below will cause:
# NameError: name 'fruits' is not defined

# print(fruits)


# --------------------------------------------------
# Extra Practice Problems
# --------------------------------------------------

# Problem 1:
# Create a tuple containing five countries and print the first and last country.

countries = ("India", "Japan", "Canada", "Germany", "Brazil")
print("First country:", countries[0])
print("Last country:", countries[-1])


# Problem 2:
# Create a tuple of numbers and print its length.

numbers = (10, 20, 30, 40, 50)
print("Tuple length:", len(numbers))


# Problem 3:
# Slice and print the middle three elements.

numbers = (1, 2, 3, 4, 5)
print("Middle three:", numbers[1:4])


# Problem 4:
# Convert a tuple into a list, add a new item, and convert it back to a tuple.

colors = ("red", "green", "blue")

colors_list = list(colors)
colors_list.append("yellow")

colors = tuple(colors_list)

print("Updated colors tuple:", colors)

# Problem 5:
# Check whether "Python" exists in the tuple.

languages = ("Python", "Java", "C++", "JavaScript")
print("Python exists:", "Python" in languages)


# Problem 6:
# Join two tuples together.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2

print("Joined numbers:", joined_tuple)