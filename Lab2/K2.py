a = str(input())
arr2 = []
for i in a:
    if(i.isalnum() == False) and (i != " "):
        a = a.replace(i, "")
arr = a.split()
arr = set(arr)
for n in arr:
    arr2.append(n)
arr2.sort()
print(len(arr2))
for j in arr2:
    print(j)