# Empty Class
class Dog:
    species = "Canis lupus familiaris"
    
    def bark(self):
        print("Woof! I demand treats immediately!")
    
    def sit(self):
        print("Fine, I'll sit. But only because there's a treat involved.")

# Object - Instance of Dog Class
dog1 = Dog()
dog2 = Dog() 

dog1.bark()
dog1.sit() 

# print(type(dog1))
# print(dog1 == dog2)