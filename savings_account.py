import json

class SavingsAccount:
    def __init__(self, name, password, balance=1000):
        self.name = name
        self.password = password
        self.balance = balance
        self.save()

    def deposit(self, amount):
        self.balance += amount
        self.save()
        print("Deposited", amount, "Current Balance", self.balance, sep=" ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("ERROR: Insufficient funds")
            return
        self.balance -= amount
        self.save()
        print("Withdrew", amount, "Current Balance", self.balance, sep=" ")

    def save(self):
        accounts = self.read_accounts()
        account_data = {"name": self.name, "password": self.password, "balance": self.balance}
        
        # Check if account exists and update it
        for acc in accounts:
            if acc['name'] == self.name:
                acc.update(account_data)
                break
        else:
            # If account doesn't exist, append a new one
            accounts.append(account_data)
        
        with open("data.json", "w") as accounts_json:
            json.dump(accounts, accounts_json, indent=3)

    @staticmethod
    def read_accounts():
        try:
            with open('data.json', 'r') as file:
                accounts = json.load(file)
                return accounts
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def find_account(name, password):
        accounts = SavingsAccount.read_accounts()
        for account in accounts:
            if account['name'] == name and account['password'] == password:
                return account
        return None
