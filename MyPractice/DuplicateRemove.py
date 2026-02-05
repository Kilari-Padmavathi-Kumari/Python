n=[1,2,3,4,5,3,2,2,1,3,2]
print(list(set(n)))

n=[1,2,3,4,5,3,2,2,1,3,2]

seen = set()  # store unique elements
duplicates = set() # store duplicates

for item in n:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("duplicate elements :",duplicates)
