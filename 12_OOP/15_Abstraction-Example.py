from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, acc_holder, acc_number, balance = 0):
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.balance = balance
        self.transaction_history = []
        
    # Abstract Methods
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def calculate_interest(self):
        pass
    
    @abstractmethod
    def minimum_balance(self):
        pass
    
    # Concrete Methods
    def deposit(self, amount):
        pass
    
    def check_balance(Self):
        pass
    
    def log_transaction(self):
        pass
    
    def print_statement(self):
        pass
    

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        pass
    
    def calculate_interest(self):
        pass
    
    def minimum_balance(self):
        pass
    
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        pass
    
    def calculate_interest(self):
        pass
    
    def minimum_balance(self):
        pass