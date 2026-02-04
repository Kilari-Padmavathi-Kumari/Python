'''
Docstring for Pure&impure.Pure
pure function:

Always returns the same output for the same input
Has no side effects (doesn’t modify external state)
'''
def add(a,b):
    return a+b
print(add(3,4))


def num(n):
    print(n*n)
num(2)