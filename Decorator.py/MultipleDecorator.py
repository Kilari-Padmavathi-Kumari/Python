def uppercase(fun):
    def wrapper():
         # Call fun() function and convert its result to uppercase
        return fun().upper()
    # Return the wrapper function
    return wrapper

def addition(fun):
    def wrapper():
        # Call fun() function and append " padma" to its result
        return fun() + " padma"
    return wrapper

@uppercase
@addition
def display():
    return "hello"
print(display())

