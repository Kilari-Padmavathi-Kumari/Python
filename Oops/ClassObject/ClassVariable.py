class Employee:
    company = "TCS"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

e1 = Employee("Padma")
e2 = Employee("vedha")

print(e1.company)
print(e2.company)


'''class Employee:
    company = "TCS"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

e1 = Employee("Padma")
e2 = Employee("Amit")

Employee.company="FissionLabs"

print(e1.company)
print(e2.company)
'''
