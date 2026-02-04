import re
rendstr="12345"
print("matches:",len(re.findall("\d{5}",rendstr)))