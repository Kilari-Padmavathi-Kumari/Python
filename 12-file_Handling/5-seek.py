'''
Docstring for 12-File-Handling
 open
 read/write
 close
'''
s=open('demo.txt',mode='w+')
s.write("w+ mode")
s.seek(0)
print(s.read())
s.close()