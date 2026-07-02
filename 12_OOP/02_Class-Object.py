# Empty Class
class Dog:
    species = "Canis lupus familiaris"
    
    def bark(self):
        print("Woof! I demand treats immediately!")
    
    def sit(self):
        print("Fine, I'll sit. But only because there's a treat involved.")
        
    def who_am_i(self):
        print(f"I am the object at memory address: {id(self)}")

# Object - Instance of Dog Class
dog1 = Dog()
dog2 = Dog() 

"""
dog1.bark()      # Dog.bark(dog1)  # This is the same as dog1.bark()
dog1.sit() 
"""

dog1.who_am_i()
dog2.who_am_i()

# print(type(dog1))
# print(dog1 == dog2)