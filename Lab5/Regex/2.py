import re
txt = str(input())
pattern = 'a[b{2, 3}].[^b]'
x = re.search(pattern, txt)
if(x == None):
    print("Not Found")
else:
    print("Found")