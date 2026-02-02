import re
num="9876543121"
if re.findall(r"^[6-9]\d{9}$",num):
    print("valid phone number")
