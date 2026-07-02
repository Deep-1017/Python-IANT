class Team:
    # members = []  # Class variable (shared list — DANGER ZONE)

    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)  # Modifying SHARED list!

team_a = Team("Avengers")
team_b = Team("Justice League")

team_a.add_member("Iron Man")
team_b.add_member("Batman")

print(team_a.members) 
print(team_b.members)