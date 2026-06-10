# mutable (Changable)
# Ordered Colection
# Allow Duplicates

my_fruits = ["apple", "banana", "cherry", "date", "apple", "banana", "elderberry"]
# print(my_fruits)
# print(len(my_fruits))

list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

# List Constructor
marks = list((10, 20, 95, 45, 68))
# print(marks[-2])

thislist = ["apple", "banana", "cherry", "orange", "apple", "melon", "mango"]


# print(thislist[2:5])

if("kiwi" in thislist):
    print("Kiwi is in the list")
    
thislist[2:4] = ['kiwi', 'litchi']
    
thislist.insert(3, "pineapple")

thislist.append("muskmelon")

thislist.extend(marks)

thislist.remove("apple")
thislist.pop(5)
# del thislist
thislist.clear()
# print(thislist)