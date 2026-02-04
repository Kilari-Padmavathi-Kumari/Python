class Bank:
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance+=amount
        print(self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('insufficient balance')
        else:
            self.balance-=amount
            print(self.balance)
    def check_Balance(self):
        print(self.balance)

b=Bank()
b.deposite(1000)
b.withdraw(500)
b.check_Balance()