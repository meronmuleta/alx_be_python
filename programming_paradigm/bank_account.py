class BankAccount:
    def __init__(self,initial_balance=0.0):
        self.account_balance = float(initial_balance)
    def deposit(self,amount):
        self.account_balance += float(amount)
        return f"Deposited: ${amount}"
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= float(amount)
            return f"Withdrew: ${amount}"
        else:
            return f"Insufficient funds."
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

