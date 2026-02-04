import re
'''
#\w ^[a-zA-Z ]+$ 

^ → start of string
[A-Za-z ] → letters + space
+ → one or more characters
$ → end of string
'''

name="padma kilari"
if re.fullmatch("[A-Za-z ]+",name):
    print("valid")
else:
    print("not valid")