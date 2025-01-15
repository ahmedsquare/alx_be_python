class BankAccount:
    def __init__(self, balance = 0):
        self.account_balance = balance

    def deposit(self, amount)->None:
        self.account_balance += amount


    def withdraw(self, amount)->bool:
        if(amount > self.account_balance):
            return False
        else:
            self.account_balance -= amount 
            return True


    def display_balance(self)->None:
        print(f"Current Balance: ${self.account_balance:.2f}") 
