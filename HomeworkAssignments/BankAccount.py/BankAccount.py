from random import randint

# creates the class BankAccount. I have it recieve a name, make an account number, and set its balance to 0.


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.accountNumber = randint(10000, 99999)
        self.balance = 0.00

# function for making deposits
    def make_deposit(self, deposit):
        self.balance += deposit

# function for making withdrawals
    def make_withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            print("You cannot withdraw more than your current balance.")
        else:
            self.balance -= withdrawal

# function for viewing account info
    def view_account_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.accountNumber}")
        print(f"Balance: ${self.balance:,.2f}\n")
