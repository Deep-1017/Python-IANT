a = 10
b = 42

# if a > b: print("a is greather than b")   
# elif a == b:
#     print("a is equal to b")
# else: 
#     print("a is less than b")

# print("a is less than b") if a < b else print("a is greather than b")

if a > b:
    pass

print(a if a > b else b)
result = a if a > b else b
print(result)