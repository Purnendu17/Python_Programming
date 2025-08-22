class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        self.balance -= amount
        return self.balance


account = BankAccount("Avani", 500)
print("Account holder:",{account.holder}, "Balance: $",{account.balance})

# Deposit money
account.deposit(200)
print("Balance after deposit: $",{account.balance})

# Withdraw money
account.withdraw(100)
print("Balance after withdrawal: $",{account.balance})