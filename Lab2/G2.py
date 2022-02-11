a = int(input())
arr_demon = []
arr_hunter = []
new_arr = []
for i in range(a):
    d = input().split()
    arr_demon.append(d)
b = int(input())
for j in range(b):
    h = input().split()
    arr_hunter.append(h)
arr_demon.sort(key = lambda x: x[1])
k = 0
while k < len(arr_hunter):
    arr_hunter[k][2] = int(arr_hunter[k][2])
    k += 1
k = 0
while k < len(arr_demon):
    l = 0
    while l < len(arr_hunter):
        
        l += 1
    k += 1
for i in arr_demon:
    print(i)
for j in arr_hunter:
    print(j)
for i in new_arr:
    print(i)