class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def calculate_salary(self):
        # manager getting bonus
        return self.salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        # Developer getting performance wise incentive
        return self.salary + 5000


employees = [
    Manager("kavya", 50000),
    Developer("Padma", 40000)
]

for emp in employees:
    print(emp.name, emp.calculate_salary())
