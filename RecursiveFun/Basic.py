def fun(n):
    if n>0:
        print(n)
        fun(n-1)
f=fun(5)
print(f)