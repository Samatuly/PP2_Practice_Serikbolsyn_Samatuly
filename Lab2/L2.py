o = ["[","{","("]
c = ["]","}",")"]
str = str(input())
arr = []
for i in str:
    if i in o:
        arr.append(i)
    elif i in c:
        p = c.index(i)
        if((len(arr) > 0) and (o[p] == arr[len(arr)-1])):
            arr.pop()
        else:
            print("No")
            exit()
if len(arr) == 0:
    print("Yes")
else:
    print("No")
print(p)