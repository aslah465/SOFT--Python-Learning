# Python Sets Practice
# Topics:
# 1. Creating a Set
# 2. Getting Set's Length
# 3. Accessing Items in a Set
# 4. Checking an Item
# 5. Adding Items to a Set
# 6. Removing Items from a Set
# 7. Clearing Items in a Set
# 8. Deleting a Set
# 9. Converting List to Set
# 10. Joining Sets
# 11. Finding Intersection Items
# 12. Checking Subset and Super Set
# 13. Checking the Difference Between Two Sets
# 14. Finding Symmetric Difference Between Two Sets


# --------------------------------------------------
# 1. Creating a Set
# --------------------------------------------------

empty_set = set()
print("Empty set:", empty_set)

fruits = {"banana", "orange", "mango", "lemon"}
print("Fruits set:", fruits)


# --------------------------------------------------
# 2. Getting Set's Length
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}
print("Number of fruits:", len(fruits))


# --------------------------------------------------
# 3. Accessing Items in a Set
# --------------------------------------------------

# Sets are unordered, so we cannot access items using an index.
# We can loop through the set instead.

fruits = {"banana", "orange", "mango", "lemon"}

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 4. Checking an Item
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

print("Is banana in fruits?", "banana" in fruits)
print("Is apple in fruits?", "apple" in fruits)


# --------------------------------------------------
# 5. Adding Items to a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.add("apple")
print("After add:", fruits)

fruits.update(["lime", "grape"])
print("After update:", fruits)


# --------------------------------------------------
# 6. Removing Items from a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("orange")
print("After discard:", fruits)


# --------------------------------------------------
# 7. Clearing Items in a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.clear()
print("After clear:", fruits)


# --------------------------------------------------
# 8. Deleting a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

del fruits

# print(fruits)
# This would give NameError because the set is deleted.


# --------------------------------------------------
# 9. Converting List to Set
# --------------------------------------------------

fruits_list = ["banana", "orange", "mango", "banana", "lemon"]

fruits_set = set(fruits_list)

print("List:", fruits_list)
print("Converted set:", fruits_set)


# --------------------------------------------------
# 10. Joining Sets
# --------------------------------------------------

fruits = {"banana", "orange", "mango"}
vegetables = {"carrot", "potato", "onion"}

food = fruits.union(vegetables)
print("Using union:", food)

fruits.update(vegetables)
print("Using update:", fruits)


# --------------------------------------------------
# 11. Finding Intersection Items
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

common_items = set_a.intersection(set_b)

print("Intersection:", common_items)


# --------------------------------------------------
# 12. Checking Subset and Super Set
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {2, 3}

print("Is set_b a subset of set_a?", set_b.issubset(set_a))
print("Is set_a a superset of set_b?", set_a.issuperset(set_b))


# --------------------------------------------------
# 13. Checking the Difference Between Two Sets
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print("Difference A - B:", set_a.difference(set_b))
print("Difference B - A:", set_b.difference(set_a))


# --------------------------------------------------
# 14. Finding Symmetric Difference Between Two Sets
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

symmetric = set_a.symmetric_difference(set_b)

print("Symmetric difference:", symmetric)


# --------------------------------------------------
# Extra Practice Problems
# --------------------------------------------------

# Problem 1:
# Create a set of five countries and print its length.

countries = {"India", "Japan", "Canada", "Germany", "Brazil"}
print("Countries:", countries)
print("Number of countries:", len(countries))


# Problem 2:
# Add a new country to the set.

countries.add("Australia")
print("After adding:", countries)


# Problem 3:
# Remove one country from the set.

countries.discard("Japan")
print("After removing Japan:", countries)


# Problem 4:
# Check if India exists in the set.

print("Is India in countries?", "India" in countries)


# Problem 5:
# Find common items between two sets.

python_students = {"Fayas", "Arun", "Rahul"}
javascript_students = {"Rahul", "Meera", "Fayas"}

common_students = python_students.intersection(javascript_students)

print("Common students:", common_students)


# Problem 6:
# Find all unique students from both sets.

all_students = python_students.union(javascript_students)

print("All students:", all_students)


# Problem 7:
# Find students who are in only one of the two sets.

unique_students = python_students.symmetric_difference(javascript_students)

print("Students in only one set:", unique_students)