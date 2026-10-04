# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# 1. Join A and B
joined = A.union(B)
print("A union B:", joined)


# 2. Find A intersection B
intersection = A.intersection(B)
print("A intersection B:", intersection)


# 3. Is A subset of B
print("Is A subset of B?", A.issubset(B))


# 4. Are A and B disjoint sets
print("Are A and B disjoint?", A.isdisjoint(B))


# 5. Join A with B and B with A
print("A union B:", A.union(B))
print("B union A:", B.union(A))


# 6. Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_difference)


# 7. Delete the sets completely
del A
del B