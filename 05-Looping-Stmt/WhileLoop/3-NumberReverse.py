n=int(input("enter a number"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    print(rev)
    n=n//10