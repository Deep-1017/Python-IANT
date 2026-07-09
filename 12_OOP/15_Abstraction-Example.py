from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount(ABC):
    def __init__(self, acc_holder, acc_number, balance = 0):
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self._balance = balance
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
        if(amount <= 0):
            print("Deposit amount must be in positive")
            return
        
        self._balance += amount
        self._log_transaction("Deposit", amount)
    
    def check_balance(self):
        print(f"{self._balance}")
        return self._balance
    
    def _log_transaction(self, txn_type, amount):
        self.transaction_history.append({
            "txn_type": txn_type,
            "amount": amount,
            "datetime": datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
            "txn_balance": self._balance
        })
    
    def print_statement(self):
        print(f"Transcation of {self.acc_holder} - {self.acc_number}")
        
        for txn in self.transaction_history:
            print(f"{txn['datetime']} - {txn['txn_type']} - {txn['amount']} - {txn['txn_balance']}")
    

class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04
    MINIMUM_BALANCE = 1000
    
    def withdraw(self, amount):
        if(amount <= 0):
            print("Withdrawal amount must be in positive")
            return
        
        if self._balance - amount < self.MINIMUM_BALANCE:
            print("Withdrawal Denied! Minimum balance must be 1000")
            return
        
        self._balance -= amount
        self._log_transaction("Withdraw", amount)
    
    def calculate_interest(self):
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
    
    def minimum_balance(self):
        return self.MINIMUM_BALANCE
    
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000
    
    def withdraw(self, amount):
        if self._balance - amount < -self.OVERDRAFT_LIMIT:
            print("Withdrawal Denied! Overdraft Limit hit.")
            return
        
        self._balance -= amount
        self._log_transaction("Withdraw", amount)
    
    def calculate_interest(self):
        print("Current Accounts do not earn interest")
    
    def minimum_balance(self):
        print("Current Accounts do not have minimum balance")