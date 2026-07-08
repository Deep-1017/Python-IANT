# Bank Account Management System

## 📌 Problem Statement

Develop a **Bank Account Management System** in Python using
**Object-Oriented Programming (OOP)** concepts. Your program should
demonstrate the use of **Abstraction, Inheritance, Encapsulation, and
Polymorphism** by implementing different types of bank accounts with
their own business rules.

The system should maintain customer account details, allow deposits and
withdrawals, calculate interest where applicable, and maintain a
transaction history.

------------------------------------------------------------------------

# 🎯 Objectives

Create a banking application that:

-   Uses an **Abstract Base Class (ABC)** to define the common structure
    of all bank accounts.
-   Creates specialized account types by inheriting from the base class.
-   Enforces different withdrawal rules for different account types.
-   Maintains a transaction history.
-   Demonstrates real-world banking operations.

------------------------------------------------------------------------

# 📋 Requirements

## 1. Create an Abstract Class `BankAccount`

The abstract class should contain the following attributes:

-   Account Holder Name
-   Account Number
-   Current Balance
-   Transaction History

------------------------------------------------------------------------

## 2. Implement the following Abstract Methods

These methods **must be declared as abstract** inside the base class.

### a) `withdraw(amount)`

Each account type will implement its own withdrawal rules.

### b) `calculate_interest()`

Each account type will calculate interest differently.

### c) `minimum_balance()`

Each account type should define its own minimum balance requirement.

------------------------------------------------------------------------

# 3. Implement Common Methods in the Base Class

The following methods should be implemented once inside the abstract
class so every account can use them.

### Deposit Money

-   Accept deposit amount.
-   Reject zero or negative values.
-   Update balance.
-   Store transaction in history.

### Check Balance

Display the current account balance.

### Log Transaction

Maintain a transaction history containing:

-   Transaction Type
-   Amount
-   Date & Time
-   Balance After Transaction

### Print Statement

Display all transactions in a formatted bank statement.

------------------------------------------------------------------------

# 4. Create `SavingsAccount` Class

This class should inherit from `BankAccount`.

### Rules

-   Annual Interest Rate = **4%**
-   Minimum Balance = **₹1000**

### Withdrawal Rules

-   Withdrawal amount must be positive.
-   Customer cannot withdraw if the remaining balance becomes less than
    ₹1000.
-   Display an appropriate error message if withdrawal is denied.

### Interest

Calculate annual interest based on the current balance and credit it to
the account.

------------------------------------------------------------------------

# 5. Create `CurrentAccount` Class

This class should inherit from `BankAccount`.

### Rules

-   No minimum balance requirement.
-   Overdraft limit = **₹5000**

### Withdrawal Rules

-   Customer can withdraw even if balance becomes negative.
-   Balance cannot go below **−₹5000**.
-   Deny withdrawal if overdraft limit is exceeded.

### Interest

Current accounts do **not** earn interest.

Display an appropriate message when interest calculation is attempted.

------------------------------------------------------------------------

# 6. Transaction History

Every successful transaction should be stored with:

-   Transaction Type
-   Amount
-   Date & Time
-   Balance after transaction

Example:

``` text
2026-07-07 11:15:32
Deposit
₹1000
Balance: ₹5000
```

------------------------------------------------------------------------

# 7. Demonstrate the Program

Create at least:

-   One Savings Account
-   One Current Account

Perform the following operations:

-   Deposit money
-   Withdraw money
-   Attempt an invalid withdrawal
-   Calculate interest
-   Print account statement

------------------------------------------------------------------------

# 📤 Expected Output (Sample)

``` text
₹500 deposited. New balance: ₹2500

Withdrawal denied.
Minimum balance of ₹1000 must be maintained.

₹1000 withdrawn.
New balance: ₹1500

Interest credited: ₹60.00

----- Statement -----

Deposit      ₹500
Withdraw     ₹1000
Interest     ₹60

Current Balance: ₹1560
```

------------------------------------------------------------------