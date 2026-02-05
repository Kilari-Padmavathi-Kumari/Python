def uppercase(fun):
    def wrapper():
        return fun().upper()
    return wrapper

def addition(fun):
    def wrapper():
        return fun() + " padma"
    return wrapper

@uppercase
@addition
def display():
    return "hello"
print(display())

