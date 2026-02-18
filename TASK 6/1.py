class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            print("Initial balance cannot be negative. Setting to 0.")
            self.__balance = 0
        else:
            self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print("Current Balance:", account.get_balance())
