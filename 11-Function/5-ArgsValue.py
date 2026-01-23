def fun(*args):
    print(args)
fun(1,2.2,'padma')          #positional args tuple variable create


def fun(*args):
    for i in args:
        print(i)
fun(1,2.2,'padma')  