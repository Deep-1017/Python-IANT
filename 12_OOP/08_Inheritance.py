class Wizard:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.spells_known = []

    def learn_spell(self, spell):
        self.spells_known.append(spell)
        print(f"{self.name} learned {spell}!")

    def introduce(self):
        print(f"I'm {self.name}, proud member of {self.house}.")
        
class Auror(Wizard):
    def hunt_dark_wizards(self):
        print(f"{self.name} is hunting dark wizards. Stay sharp.")
        
class child(Auror):
    pass
        
harry = Auror("Harry Potter", "Gryffindor")
harry.introduce()
harry.learn_spell("Expelliarmus")
harry.hunt_dark_wizards()