n = int(input())
arr = []
i = 0
while i < n:
    a = str(input())
    arr.append(a)
    i += 1
i = 0
for x in arr:
    if("@gmail.com" in arr[i]):
        print(arr[i].replace('@gmail.com', ''))
    i += 1
