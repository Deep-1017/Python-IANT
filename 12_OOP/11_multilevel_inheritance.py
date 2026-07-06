class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        
class Father(Grandfather):
    def __init__(self, grandfathername, fathername):
        super().__init__(grandfathername)
        self.fathername = fathername
        
class Son(Father):
    def __init__(self, grandfathername, fathername, sonname):
        super().__init__(grandfathername, fathername)
        self.sonname = sonname
        
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

        
chintu = Son("Ramesh", "Suresh", "Chinmay")

# chintu.grandfathername = "Ramesh"
# chintu.fathername = "Suresh"
# chintu.sonname = "Chinmay"

chintu.print_name()

