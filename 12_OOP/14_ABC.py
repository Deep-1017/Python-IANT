from abc import ABC, abstractmethod

class Spell(ABC):                  # ABC = Abstract Base Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cast(self):                # No body — subclasses MUST define this
        pass
    
class Expelliarmus(Spell):
    def cast(self):
        print(f"{self.name}! The opponent's wand flies away.")
        
class Lumos(Spell):
    def cast(self):
        print(f"{self.name}! The wand tip lights up.")
        
# spell = Spell("Generic Spell")   # TypeError! Can't instantiate an abstract class

        
e = Expelliarmus("Expelliarmus")
e.cast()
l = Lumos("Lumos")
l.cast()