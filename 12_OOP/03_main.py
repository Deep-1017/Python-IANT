class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def introduce(self):
        print(f"Hi! I'm {self.name}, a {self.age}-year-old {self.breed}.")
        print(f"My hobbies are: barking at the mailman and napping.")
        
bruno = Dog("Bruno", "Labrador", 3)
tommy = Dog("Tommy", "Poodle", 5) 

bruno.introduce()
tommy.introduce() 