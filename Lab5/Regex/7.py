import re
txt = str(input())
i = 0
while i < len(txt):
    if(txt[i] == "_"):
        lt = txt[i + 1]
        lt = lt.upper()
    i += 1
if("_" in txt):
    x = re.sub("[_][a-z]", lt, txt)
else:
    print("Impossible")
    exit(0)
print(x)