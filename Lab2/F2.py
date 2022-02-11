dict = {}
arr = []
arr2 = []
a = int(input())
for i in range(a):
    b = input().split()
    if b[0] not in dict:
        dict[b[0]] = int(b[1])
    else:
        dict[b[0]] += int(b[1])
mx = 0
for i in dict.values():
    i = int(i)
    if(i > mx):
        mx = i
for j in dict:
    c = int(mx) - int(dict[j])
    if(dict[j] == mx):
        arr.append(j + ' is lucky!')
        arr2.append(arr)
        arr = []
    else:
        arr.append(j + ' has to receive')
        arr.append(c)
        arr.append('tenge')
        arr2.append(arr)
        arr = []
arr2.sort()
for i in arr2:
    print(*i)