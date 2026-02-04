def Outer(f):
    def inner():
        print("function is running")
        result=f()
        return result
    return inner
@Outer
def add():
    return 10+20
print(add())