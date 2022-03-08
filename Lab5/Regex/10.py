import re
def change_case(txt):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
     
txt = str(input())
print(change_case(txt))