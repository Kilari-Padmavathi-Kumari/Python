def outer():
    print("this is outer class")
    def inner():
        print("this is inner class")
    inner()
outer()