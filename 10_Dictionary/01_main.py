# Ordered Collection
# Mutable (Changeable)
# Not allow duplicates

dict1 = {
    "name": "Deep",
    "age": 24,
    "subjects": ['maths', 'biology'],
    "isPass": True
}

# print(dict1["age"])
# print(dict1.get("subjects"))

# print(dict1.keys())
# print("Before: ", dict1.values())

# dict1["age"] = 30
dict1.update({"name": "John"})    

# print("After: ", dict1.values())

print(dict1.items())


thisdict = dict(name = "John", age = 36, country = "Norway")

# print(thisdict)