import math  # imports math module

PI = 3.14  # constant value

student_name = "Anil"  # stores student name
marks = 72  # stores marks

result = "Pass" if marks >= 50 else "Fail"  # checks pass or fail using ternary

square = lambda x: x * x  # lambda function to find square

numbers = [1, 2, 3, 4, 5]  # list of numbers
even_numbers = [i for i in numbers if i % 2 == 0]  # list comprehension for even numbers

marks_dict = {"Anil": 72, "Ravi": 45}  # dictionary storing marks
status_dict = {k: "Pass" if v >= 50 else "Fail" for k, v in marks_dict.items()}  # dict comprehension

for i in range(3): print(i)  # one-line for loop

def add(a, b): return a + b  # one-line function definition

total = add(10, 20)  # function call

sqrt_value = math.sqrt(25)  # finds square root using math module

class Student: pass  # empty class definition

print(student_name, marks, result)  # prints student details
