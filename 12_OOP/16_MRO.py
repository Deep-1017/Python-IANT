class Broomstick:
    def move(self):
        print("Flying through the air on a broomstick.")
        
    def m1(self):
        print("Hi")

class Wand:
    def move(self):
        print("Apparating with a flick of the wand.")
        
    def m2(self):
        print("Hello")

class Wizard(Wand, Broomstick):   # Inherits from BOTH
    pass


harry = Wizard()
harry.move() 
harry.m1()