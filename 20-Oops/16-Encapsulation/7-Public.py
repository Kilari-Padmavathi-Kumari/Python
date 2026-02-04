class Student:
    def __init__(self, name, marks):
        self.name = name      # public variable
        self.marks = marks    # public variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

# object creation
s1 = Student("Padma", 85)

# accessing public variables
print(s1.name)
print(s1.marks)

# calling method
s1.display()
