account_name = "Harry"
account_balance = 5000
account_pin = 1234

# an1 = "Deep"
# ab1 = 200
# ap1 = 123

# ab2
# an2
# ap2

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount, pin, entered_pin):
    if pin == entered_pin:
        return balance - amount
    else:
        print("Wrong PIN! Nice try, thief.")
        return balance

account_balance = deposit(account_balance, 1000)
print(account_balance)  # 6000

account_balance = withdraw(account_balance, 500, account_pin, 1234)
print(account_balance)  # 5500