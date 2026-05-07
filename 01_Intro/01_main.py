# print("Hello, World!", end=" $ ")
# print("Hii", end=" $ ")
# print("How are you?") 

if (10 > 20):
    print("10 > 20")


# Variable Define
name = "Deep"
Name = "John"
# print(name) 

# print(123 + 12) 

# print("Hello, I am ", 23, " Years old")


# firstName = "Alice"
# FirstName = "John"
# first_name = "Ann"

first_name, firstName, FirstName = "Jonh", "Alice", "Ann"

# global variables
a = b = c = 10

def greet():
    global d, name, a
    d = 45
    name = "hi"
    a = 12
    print("Inside func", a)


greet()
# print(d)
# print(name)

print("Outside func", a)