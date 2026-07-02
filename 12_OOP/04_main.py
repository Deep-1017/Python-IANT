class Coffee:
    def __init__(self, name, sugar=2, milk=True, extra_shot=False):
        self.name = name
        self.sugar = sugar
        self.milk = milk
        self.extra_shot = extra_shot
        
    def describe(self):
        shot_text = "double shot" if self.extra_shot else "single shot"
        milk_text = "with milk" if self.milk else "black"
        print(f"{self.name}: {shot_text}, {self.sugar} sugars, {milk_text}")
        
my_coffee = Coffee("Latte", sugar=1, extra_shot=True)
boss_coffee = Coffee("Espresso", sugar=0, milk=False)
intern_coffee = Coffee("Caramel Frappuccino", sugar=5)

my_coffee.describe()
boss_coffee.describe()
intern_coffee.describe()