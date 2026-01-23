'''
Docstring for 13-ExceptionHandling.py.1-Basic

| Exception         | Reason               |
| ----------------- | -------------------- |
| ZeroDivisionError | Divide by zero       |
| ValueError        | Invalid value        |
| TypeError         | Wrong data type      |
| IndexError        | Index out of range   |
| KeyError          | Key not found        |
| FileNotFoundError | File missing         |
| NameError         | Variable not defined |

'''
a=1

try:
    print(b)
except:
    print("Error")
else:
    print("no error")
finally:
    print("always")