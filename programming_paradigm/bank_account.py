class BankAccount:
    def __init__(self, balance: float = 0):
        self.account_balance = balance

    def deposit(self, amount:float)->None:
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")


    def withdraw(self, amount:float)->bool:
        if(amount > self.account_balance):
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount 
            print(f"Withdrew: ${amount:.1f}")
            return True


    def display_balance(self)->None:
        print(f"Current Balance: ${self.account_balance:.2f}") 
