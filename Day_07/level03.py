# 1. Convert ages to a set and compare the length

ages = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Length of list:", len(ages))
print("Length of set:", len(ages_set))

if len(ages) > len(ages_set):
    print("The list is bigger")
elif len(ages) < len(ages_set):
    print("The set is bigger")
else:
    print("Both are equal")