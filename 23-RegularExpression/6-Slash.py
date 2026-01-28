'''
Docstring for 23-RegularExpression.6-Slash
\b -> backspace
\f -> formfeed
\r -> carriage return
\t -> tab
\v -> vertical tab
'''

import re
randstr='''
keep the blue flag
flying high
chelsea
'''

print(randstr)

regex=re.compile("\n")
randstr=regex.sub(" ",randstr)
print(randstr)