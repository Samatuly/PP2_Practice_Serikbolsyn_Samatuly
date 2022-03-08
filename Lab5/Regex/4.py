import re
txt = str(input())
pattern = '[A-Z][a-z]'
x = re.findall(pattern, txt)
if(x == None):
    print("Not found")
else:
    print(x)