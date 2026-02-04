'''import math
data=[1,2,2,3,4,4,5,6,7,7]
set1=set(data)
print(set1)
for i in set1:
    if i%2==1:
        print(math.sqrt(i))'''


data=[1,2,2,3,4,4,5,6,7,7]
data1={x*x for x in data if x%2!=0 and x*x>10}
print(data1)
