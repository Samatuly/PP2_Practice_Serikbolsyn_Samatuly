dates = []
i = 1
while i > 0:
    arr = input()
    if(arr == '0'):
        i -= 1
        break
    a = arr.split()
    dates.append(a)
dates.sort(key = lambda x: (x[2], x[1], x[0]))

for j in dates:
    print(*j, end = " ")
    print()
