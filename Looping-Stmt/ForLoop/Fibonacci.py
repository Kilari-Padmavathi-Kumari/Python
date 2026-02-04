n=int(input("Enter a number"))
a=0
b=1
for i in range(0,n):
    sum=a+b
    a=b
    b=sum
    print(a)