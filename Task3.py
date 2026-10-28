class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )
        self.balance = self.balance - amount
        print(f"{self.owner} withdrew {amount}")

    def show(self):
        print("Account Owner:", self.owner)
        print("Current Balance:", self.balance)


acc = Account("Sathish", 1000)

try:
    acc.deposit(500)
    acc.withdraw(2000)
except InsufficientFundsError as error:
    print("Error:", error)
finally:
    print("Transaction finished")
