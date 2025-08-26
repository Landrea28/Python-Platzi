class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
        self.isActive = True  # Initialize account as active

    def deposit(self, amount):
        if self.isActive:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Account is inactive. Cannot deposit.")

    def withdraw(self, amount):
        if self.isActive:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account is inactive. Cannot withdraw.")

    def deactivate(self):
        self.isActive = False
        print("Account deactivated.")

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

#llamada de metodos
account1.deposit(500)
account2.deposit(300)

account1.withdraw(200)
account2.withdraw(100)

account1.deactivate()
account1.deposit(100)
