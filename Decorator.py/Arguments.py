def my_decotaror(fun):
    def wrapper(*args,**kwargs):
        print("Before function execution")
        fun(*args,**kwargs)
        print("After function execution")
    return wrapper

@my_decotaror
def add(a,b):
    print(a+b)

add(3,4)