'''a = "education"
c = 0

for ch in a:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        c += 1

print(c)'''

a='education'
count=0
vowels="aeiouAEIOU"

for ch in a:
    if ch in vowels:
        count+=1
print(count)

