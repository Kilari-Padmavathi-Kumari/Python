class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

acc = BankAccount("Padma", 10000)

#  cannot access private variable directly
# print(acc.__balance)  # AttributeError

# access through methods
acc.show_balance()
acc.deposit(2000)
acc.withdraw(3000)
acc.show_balance()
