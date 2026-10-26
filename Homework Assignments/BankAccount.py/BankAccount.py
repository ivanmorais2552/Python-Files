from random import randint


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.accountNumber = randint(10000, 99999)
        self.balance = 0.00


#  Make a deposit
# 2. Make a withdrawal
# 3. View account information

    def make_deposit(self, deposit):
        self.balance += deposit

    def make_withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            print("You cannot withdraw more than your current balance.")
        else:
            self.balance -= withdrawal

    def view_account_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.accountNumber}")
        print(f"Balance: ${self.balance:,.2f}\n")
