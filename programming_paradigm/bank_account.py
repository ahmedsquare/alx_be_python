class BankAccount:
    def __init__(self, balance = 0):
        self.account_balance = balance

    def deposit(self, amount)->None:
        self.account_balance += amount
        print(f"Deposited: ${amount}")


    def withdraw(self, amount)->None:
        if(amount > self.account_balance):
            print("Insufficient funds.")
        else:
            self.account_balance -= amount 
            print(f"Withdrew: ${amount}")


    def display_balance(self)->None:
        print(f"Current Balance: ${self.account_balance}") 
