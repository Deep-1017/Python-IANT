# print(dir(int))

class Galleon:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} Galleons"          # for print() and str()

    def __repr__(self):
        return f"Galleon({self.amount})"           # for debugging, in the shell

    def __add__(self, other):
        return Galleon(self.amount + other.amount) # makes + work!

    def __eq__(self, other):
        return self.amount == other.amount         # makes == work!

    def __lt__(self, other):
        return self.amount < other.amount          # makes < work!

    def __len__(self):
        return self.amount                          # makes len() work!

vault1 = Galleon(500)
vault2 = Galleon(300)

print(vault1)                
print(vault1 + vault2)        
print(vault1 == Galleon(500)) 
print(vault1 > vault2)        
print(len(vault1))       