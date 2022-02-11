arr = []
arr2 = []
i = 1
while i > 0:
    a = int(input())
    if(a == 0):
        i -= 1
    else:
        arr.append(a)
if(len(arr) % 2 == 1):
    lim = (len(arr)//2) + 1
else:
    lim = (len(arr)//2)
i = 0
while i < lim:
    if(i != (len(arr) - 1 - i)):
        b = arr[i] + arr[len(arr) - 1 - i]
    else:
        b = arr[i]
    arr2.append(b)
    i += 1
print(*arr2, end = " ")