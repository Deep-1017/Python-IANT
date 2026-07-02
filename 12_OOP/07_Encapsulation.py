class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private — double underscore
        self.__pin = None
        
    def set_pin(self, pin):
        self.__pin = pin
        print("PIN set. Don't write it on a sticky note.")
        
    def get_balance(self, pin):
        if self.__pin == pin:
            return self.__balance
        print("Wrong PIN. This isn't your account, nice try.")
        return None
        
acc1 = BankAccount("Alice", 1000)
acc1.set_pin("1234")
balance = acc1.get_balance("1234")
print(balance)

print(acc1.__balance) 