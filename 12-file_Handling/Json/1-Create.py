import json 
data={'name ':'padma','age':23}
file=open ('jsondemo.json','w')
json.dump(data,file,indent=4)