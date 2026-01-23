def fun(x):
    return x*2
k=fun(4)
print(k)


k=lambda x:x*2
print(k(6))

print((lambda x:x+2)(5))

l1=[1,3,2,34,5,56,67,7]
f=filter(lambda x:x%3==0 ,l1)
l2=list(f)
print(l2)

l1=[1,2,1,3,6,9]
l2=list(map(lambda x:-x,l1))
print(l2)

l1=[1,2,1,3,6,9]
k=lambda x:x if x%2==0 else -x
l2=list(map(k,l1))
print(l2)

l1=[[4,2,'six'],[1,4,'five'],[3,4,'three']]
l2=sorted(l1)
print(l2)

l1=[[4,2,'six'],[1,4,'five'],[3,4,'three']]
l2=sorted(l1,key=lambda x:x[0]+x[1])
print(l2)