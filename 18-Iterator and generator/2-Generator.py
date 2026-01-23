def myRange(n):
    i=0
    while i<n:
        yield i
        i=i+1
m=myRange(4)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
#print(next(m))