fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for fruit in fruits:
#     if "a" in fruit:
#         newlist.append(fruit)

newlist = [x for x in fruits if "a" in x]
        
print(newlist)