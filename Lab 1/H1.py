s = str(input())
t = str(input())
arr = []
i = 0
for x in s:
    if(x == t):
        arr.append(i)
    i += 1  
i = 0
m = len(arr)
while(i < m):
    if(i == 0) or (i == m - 1):
        print(arr[i], end = " ")
    i += 1
