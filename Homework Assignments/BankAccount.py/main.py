from BankAccount import BankAccount as ba

print("\nWelcome to IRM Bank\n")
user = ba(input("Enter your name: "))

print("\nPlease choose an option")

while True:
    print("\n1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit\n")

    choice = input()
    if choice == "1":
        user.make_deposit(float(input(
            "How much would you like to deposit? ")))
        continue
    elif choice == "2":
        user.make_withdrawal(float(input(
            "How much would you like to withdraw? ")))
        continue
    elif choice == "3":
        user.view_account_info()
        continue
    elif choice == "4":
        print("Thank you for your business!")
        break
    else:
        print("Invalid Input. Please try again.")
