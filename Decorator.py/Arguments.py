def my_decotaror(fun):
    def wrapper(*args,**kwargs):
        # Wrapper function accepts any number of arguments
        # *args  -> positional arguments
        # **kwargs -> keyword arguments
        print("Before function execution")
        # Calling the original function with its arguments
        fun(*args,**kwargs)
        print("After function execution")
    # Return the wrapper function
    return wrapper

# Applying decorator to add() function
@my_decotaror
def add(a,b):
    print(a+b)
# Calling the decorated function
add(3,4)