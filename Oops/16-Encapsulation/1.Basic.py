'''
Docstring for Oops.16-Encapsulation.1.Basic
wrapping of variable & methods in to a single unit

private  __
protect  _
public
'''
'''class Demo():
    __a=2
    _b=10
    print(__a)
    print(_b)'''

class Demo():
    __a=2
    _b=10
    print(__a)
    print(_b)
class Demo2(Demo):
    print(_b)
    print(__a)
   
