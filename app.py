# main.py
from savings_account import SavingsAccount

def welcome_message():
    print("\n============================")
    print(" Welcome to The ABC Bank! ")
    print("============================")
    print("How can we help you today?\n")

def main_menu():
    print("---------- Main Menu ----------")
    print("Press 1 to login to your account")
    print("Press 2 to create a new account")
    print("Press 3 to exit the program")
    print("-------------------------------")


# login Makes an attempt to login a user in name and password lookup and validation.
def login(state):
    name = input("Enter your name: ")
    pwd = input("Enter your password: ")
    account_data = SavingsAccount.find_account(name, pwd)
    
    if account_data:
        print("\nLogging you in...\n")
        # Change the state to reflect login of a user, to show only account menu prompts.
        state["running"] = True
        account = SavingsAccount(name, pwd, account_data['balance'])
        account_menu(account,state)
    else:
        print("ERROR: Incorrect Name or Password\n")

# create_account Creates a new savings account for a user after very basic validation.
def create_account():
    print("\n---------- Create Account ----------")
    name = input("Enter your name: ")
    if not name:
        print("ERROR: Name cannot be empty!\n")
        return
    
    pwd = input("Enter your password: ")
    if not pwd:
        print("ERROR: Password cannot be empty!\n")
        return
    
    deposit_amount = input("Enter some deposit amount (default: 1000): ")
    if deposit_amount:
        deposit_amount = float(deposit_amount)
        if deposit_amount >= 1000:
            new_account = SavingsAccount(name, pwd, deposit_amount)
            print("New account for user", name, "created successfully!\n")
        else:
            print("ERROR: Minimum deposit amount 1000 is compulsory.\n")
    else:
        print("Depositing 1000 to your account.")
        new_account = SavingsAccount(name, pwd)
        print("New account for user", name, "created successfully!\n")
    print("-------------------------------------")

# account_menu Prompts a logged in user for viewing and changing their account data.
def account_menu(account,state):
    while True:
        print("\n-------- Account Menu --------")
        print("Press 1 to deposit")
        print("Press 2 to withdraw")
        print("Press 3 to check balance")
        print("Press 4 to logout")
        print("------------------------------")
        action = input("Your Response: ")
        
        if action == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == "3":
            print("\n==============================")
            print(f" Current Balance: {account.balance} ")
            print("==============================\n")
        elif action == "4":
            # Logout the user and change the state to prompt the user back to main menu.
            print("Logging out...\n")
            state["running"] = False
            break
        else:
            print("Invalid option. Please try again.\n")



def main(state):
    welcome_message()
    while True:
        # If a bank user is logged in, then don't show the main menu prompts.
        if state["running"] == False:
            main_menu()
        user_input = input("Your Response: ")

        if user_input == "1":
            login(state)
        elif user_input == "2":
            create_account()
        elif user_input == "3":
            print("Exiting the program. Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main(state = {"running":False})
