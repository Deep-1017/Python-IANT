dict1 = {
    "name": "Deep",
    "age": 24,
    "subjects": ['maths', 'biology'],
    "isPass": True,
}

dict2 = dict1.copy()
print(dict2)

dict1["email"] = "deep@gmail.com"

# print(dict1["name"])

for i in dict1:
    pass
    # print(f"{i}:, {dict1[i]}") 
    
for i in dict1.values():
    pass
    # print(i)
    
for i, j in dict1.items():
    # print(f"{i}: {j}")
    pass    