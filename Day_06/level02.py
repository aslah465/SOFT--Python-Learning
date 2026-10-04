# 1. Unpack siblings and parents from family_members

family_members = ("Arun", "Rahul", "Anu", "Meera", "Father", "Mother")

*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)


# 2. Create fruits, vegetables and animal products tuples
# Join them and assign to food_stuff_tp

fruits = ("banana", "orange", "mango")
vegetables = ("carrot", "potato", "onion")
animal_products = ("milk", "meat", "butter")

food_stuff_tp = fruits + vegetables + animal_products

print("Food stuff tuple:", food_stuff_tp)


# 3. Convert food_stuff_tp tuple to a list

food_stuff_lt = list(food_stuff_tp)

print("Food stuff list:", food_stuff_lt)


# 4. Slice out the middle item or items

middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index]

print("Middle item:", middle_item)


# 5. Slice out first three and last three items

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)


# 6. Delete food_stuff_tp tuple completely

del food_stuff_tp

# print(food_stuff_tp)
# This will give NameError because the tuple is deleted.


# 7. Check if an item exists in tuple

nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)

print("Is Estonia a Nordic country?", "Estonia" in nordic_countries)
print("Is Iceland a Nordic country?", "Iceland" in nordic_countries)