a = int(input())
arr = []
f_arr = []
for i in range(a):
    b = input().split()
    if b[0] == '1':
        arr.append(b[1])
    else:
        if len(arr) == 0:
            pass
        else:
            f_arr.append(arr.pop(0))
print(*f_arr)