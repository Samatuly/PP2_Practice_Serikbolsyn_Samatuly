import re
def cap(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
txt = str(input())
print(cap(txt))