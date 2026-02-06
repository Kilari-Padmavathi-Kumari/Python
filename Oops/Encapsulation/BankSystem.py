class BankAccount:
    bank_name = "SBI"   # class variable (shared)

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   # private variable (encapsulation)

    def deposit(self, amount):
      
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# object creation
acc = BankAccount("Padma", 5000)

acc.deposit(2000)
acc.withdraw(1000)

print(acc.get_balance())   # 6000
