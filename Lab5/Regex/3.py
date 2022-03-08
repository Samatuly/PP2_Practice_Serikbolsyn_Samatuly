import re
txt = str(input())
pattern = '[a-z][_]'
x = re.findall(pattern, txt)
if(x == None):
    print("Not found")
else:
    print(x)