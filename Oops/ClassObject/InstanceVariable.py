class Employee:
    def __init__(self, name, salary):
        self.name = name        # instance variable
        self.salary = salary    # instance variable

# creating objects
e1 = Employee("Padma", 40000)
e2 = Employee("josh", 50000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)
