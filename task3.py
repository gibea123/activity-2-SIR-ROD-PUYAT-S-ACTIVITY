class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number, self.owner, self.balance = account_number, owner, balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₱{amount}. Balance: ₱{self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ₱{amount}. Balance: ₱{self.balance}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Balance: ₱{self.balance}")

account = BankAccount("12345678", "GIBEA ATIENZA", 50000)
account.deposit(2000)
account.withdraw(1000)
account.display_balance()
