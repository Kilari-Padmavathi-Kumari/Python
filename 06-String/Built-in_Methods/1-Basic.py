'''
Docstring for 06-String.1-Basic
collection character in Quotes
ex 'hi'
   "padma's"
   '"padma"'
'''
a="padma"
print(a.upper())

k="kavya josh"
print(k.endswith("sh"))
print(k.startswith("p"))
print(k.replace("josh","vedha"))
print(k.index("kavya"))
print(k.find("padma"))           #-1
print(k.count(a))
print(k.removeprefix("kavya"))
print(k.split())
print(len(k))
print(k.strip())        # remove space in staring(rstrip) or ending(lstrip)