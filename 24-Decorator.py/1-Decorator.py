def outer(f):
    def inner():
        print('+' * 10)
        f()
        print('+' * 10)
    return inner    #  return function reference

@outer
def display():
    print('welcome')

display()
