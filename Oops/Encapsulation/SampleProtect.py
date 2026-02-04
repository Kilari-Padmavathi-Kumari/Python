class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected variable
        self.name = name

    def show(self):
        print("Name:", self.name)
        print("Salary:", self._salary)

emp = Employee("Anil", 50000)

# accessing protected variable (possible but not recommended)
print(emp._salary)

emp.show()
