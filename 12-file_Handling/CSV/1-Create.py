'''import csv
file=open("csvdemo.csv",'w')
writer=csv.writer(file)
writer.writerow(['name','age'])
writer.writerow(['padma','12'])
writer.writerow(['bhanu','13'])
'''

import csv

rows=[
    ['name','age'],
    ['padma',23],
    ['kavya',22]

]
file=open("csvdemo.csv",'w')
writer=csv.writer(file)
writer.writerow(rows)
