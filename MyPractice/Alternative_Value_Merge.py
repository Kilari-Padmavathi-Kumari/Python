'''
Docstring for MyPractice.Alternative_Value_Merge
1)Alternate Values from Multiple Lists (Round Robin)
Write a function that takes two lists and returns a new list by alternating elements from each list.
If one list is longer than the other, append the remaining elements at the end.
Example:
a = [1, 2]
b = ['a', 'b', 'c']

# Expected:
# [1, 'a', 2, 'b', 'c']
'''
a = [1, 2]
b = ['a', 'b', 'c']

rev=[]
for i in range(min(len(a),len(b))):
    rev.append(a[i])
    rev.append(b[i])
rev.extend(a[i+1:])
rev.extend(b[i+1:])
print(rev)