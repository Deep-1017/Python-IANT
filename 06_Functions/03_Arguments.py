def kidsCollection(*kids):
    print(kids[2])
    
# kidsCollection("john", "alice", "jack", "ann")


# Arbitary Arguments (*args)
def sumOfNumbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(total)

# sumOfNumbers(10, 20, 30, 40, 50, 60, 8)




# Arbitary Keyword Arguments (**kwargs)
def my_function(**myvar):
    print(myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")