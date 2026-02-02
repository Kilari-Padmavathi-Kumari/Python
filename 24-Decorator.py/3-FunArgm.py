def Outer(f):
    def inner(a,b):
        print("Arguments are ", a,b)
        return f(a,b)
    return inner
@Outer
def add(a,b):
    return a+b
print(add(3,4)) 