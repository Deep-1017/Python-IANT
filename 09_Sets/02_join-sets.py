set1 = {"a", "b", "c", 3, 4, 5}
set2 = {1, 2, 3, "a", "b"}

# union of set
set3 = set1.union(set2)
print(set3)

# union of set using | operator
# set4 = set1 | set2

# Intersection of set
set4 = set1.intersection(set2)
print(set4)

# Intersection of set using & operator
# set5 = set1 & set2

# Difference of set
set5 = set1.difference(set2)
print(set5)

# Difference of set using - operator
# set6 = set1 - set2

# Symmetric difference of set
set6 = set1.symmetric_difference(set2)
print(set6)