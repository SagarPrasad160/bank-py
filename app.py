# main.py
from savings_account import SavingsAccount

def welcome_message():
    print("Welcome to The ABC Bank!")
    print("How can we help you today?")

def main_menu():
    print("\nPress 1 to login to your account")
    print("Press 2 to create a new account")
    print("Press 3 to exit the program")

def login():
    name = input("Enter your name: ")
    pwd = input("Enter your password: ")
    account_data = SavingsAccount.find_account(name, pwd)
    
    if account_data:
        print("Logging you in...")
        account = SavingsAccount(name, pwd, account_data['balance'])
        account_menu(account)
    else:
        print("Incorrect Name or Password")

def create_account():
    print("Creating your account")
    name = input("Enter your name: ")
    if not name:
        print("ERROR: Name cannot be empty!")
        return
    
    pwd = input("Enter your password: ")
    if not pwd:
        print("ERROR: Password cannot be empty!")
        return
    
    deposit_amount = input("Enter some deposit amount (default: 1000): ")
    if deposit_amount:
        deposit_amount = float(deposit_amount)
        if deposit_amount >= 1000:
            new_account = SavingsAccount(name, pwd, deposit_amount)
            print("New account for user", name, "created successfully!", sep=" ")
        else:
            print("ERROR: Minimum deposit amount 1000 is compulsory.")
    else:
        print("Depositing 1000 to your account.")
        new_account = SavingsAccount(name, pwd)
        print("New account for user", name, "created successfully!", sep=" ")

def account_menu(account):
    while True:
        print("\nPress 1 to deposit")
        print("Press 2 to withdraw")
        print("Press 3 to check balance")
        print("Press 4 to logout")
        action = input("Your Response: ")
        
        if action == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == "3":
            print("Current Balance:", account.balance)
        elif action == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    welcome_message()
    while True:
        main_menu()
        user_input = input("Your Response: ")

        if user_input == "1":
            login()
        elif user_input == "2":
            create_account()
        elif user_input == "3":
            print("Exiting the program. Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
