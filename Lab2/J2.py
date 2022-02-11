a = int(input())
arr = []
arr2 = []
for i in range(a):
    x = str(input())
    alpha = x.isalpha()
    alnum = x.isalnum()
    num = x.isdigit()
    res = [char for char in x if char.isupper()]
    if(alpha == False) and (alnum == True) and (num == False):
            arr.append(x)
arr = set(arr)
for i in arr:
    for k in i:
        if(k.isupper() == True):
            arr2.append(i)
            break
print(len(arr2))
arr2.sort()
for j in arr2:
    print(j)
