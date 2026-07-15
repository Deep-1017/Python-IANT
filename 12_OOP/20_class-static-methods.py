class WizardID:
    total_issued = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        WizardID.total_issued += 1
        
    @classmethod
    def from_string(cls, data_string):
        # Alternate constructor — builds an object from a "Name-House" string
        name, house = data_string.split("-")
        return cls(name, house) 
    
    @staticmethod
    def is_valid_house(house):
        # Doesn't need self OR cls — it's just a utility function living here
        valid_houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
        return house in valid_houses
    
# Normal way to create one
id1 = WizardID("Luna Lovegood", "Ravenclaw")
# print(id1.name)
# print(id1.house)

# Factory way — useful when your data arrives as a raw string, e.g. from a file
id2 = WizardID.from_string("Deep-Slytherin")
# print(id2.name, id2.house)

# # Utility check, no object needed at all
print(WizardID.is_valid_house("Gryffindor"))   # True
print(WizardID.is_valid_house("Durmstrang"))   # False

print(WizardID.total_issued)  # 2