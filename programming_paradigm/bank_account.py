class BankAccount:
    def __init__(self, balance: float = 0):
        self.account_balance = balance

    def deposit(self, amount: float)->None:
        self.account_balance += amount
        print(f"Deposited: ${amount}")


    def withdraw(self, amount: float)->None:
        if(amount > self.account_balance):
            print("Insufficient funds.")
        else:
            self.account_balance -= amount 
            print(f"Withdrew: ${amount}")


    def display_balance(self)->None:
        print(f"Current Balance: ${self.account_balance}") 
