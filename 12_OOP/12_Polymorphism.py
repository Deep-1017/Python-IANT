class Creature:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes some generic creature noise.")
        
class Dragon(Creature):
    def make_sound(self):
        print(f"{self.name} ROARS and breathes fire. Run.")

class Pixie(Creature):
    def make_sound(self):
        print(f"{self.name} giggles mischievously and steals your socks.")

class Phoenix(Creature):
    def make_sound(self):
        print(f"{self.name} sings a hauntingly beautiful melody.")
        

# s1 = Dragon("Norbert")
# s2 = Pixie("Tinker")
# s3 = Phoenix("Fawkes")

# s1.make_sound()
# s2.make_sound()
# s3.make_sound()

creatures = [Dragon("Norbert"), Pixie("Tinker"), Phoenix("Fawkes")] 

for creature in creatures:
    creature.make_sound() 