class Magical:               # The top of the diamond
    def greet(self):
        print("I am a magical being.")

class Wizard(Magical):       # Left side of the diamond
    def greet(self):
        print("I am a wizard.")

class Elf(Magical):          # Right side of the diamond
    def greet(self):
        print("I am an elf.")

class HalfElfWizard(Wizard, Elf):   # Bottom of the diamond — inherits from BOTH
    pass

dobby = HalfElfWizard()
dobby.greet() 

print(HalfElfWizard.__mro__)