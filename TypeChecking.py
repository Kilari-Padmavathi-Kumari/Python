from typing import List, Dict, Optional, Union, Callable
from dataclasses import dataclass

# -------- BASIC TYPE HINTS --------
age: int = 25  # integer type
name: str = "Anil"  # string type
is_active: bool = True  # boolean type

# -------- FUNCTION TYPE HINTS --------
def add(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b

# -------- LIST, DICT TYPE HINTS --------
marks: List[int] = [80, 90, 75]  # list of integers
results: Dict[str, str] = {"Anil": "Pass", "Ravi": "Fail"}  # dict with str keys & values

# -------- OPTIONAL TYPE --------
email: Optional[str] = None  # string or None

# -------- UNION TYPE --------
value: Union[int, str] = 100  # can be int or string

# -------- CALLABLE TYPE --------
def multiply(a: int, b: int) -> int:
    return a * b

def apply_operation(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Apply a function to two integers."""
    return func(x, y)

# -------- DATACLASS WITH TYPE HINTS --------
@dataclass
class Student:
    name: str
    marks: int

# -------- USING ALL ABOVE --------
total = add(10, 20)  # function call
product = apply_operation(multiply, 3, 4)  # callable usage
student = Student(name="Anil", marks=85)  # object creation

# -------- OUTPUT --------
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Total:", total)
print("Product:", product)
print("Student:", student)
