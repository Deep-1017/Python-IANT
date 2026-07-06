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
        
class DarkWizard(Wizard):
    def __init__(self, name, house, dark_mark=True):
        # self.name = name
        # self.house = house
        # self.spells_known = []
        super().__init__(name, house) 
        
    def introduce(self):
        print(f"{self.name}, {self.house}, {self.dark_mark}")
        
        
harry = DarkWizard("Harry", "dubh", False)
harry.introduce()