import re
txt = str(input())
pattern = '[a].*[b]$'
x = re.search(pattern, txt)
if(x == None):
    print("Not found")
else:
    print("Found")