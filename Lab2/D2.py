x = int(input())
arr = []
row = col = x
oj = x - 1
ej = 0
for i in range(row):
    a = []
    for j in range(col):
        if(x % 2 == 1):
            if(j >= oj):
                b = '#'
            else:
                b = '.'
        if(x % 2 == 0):
            if(j <= ej) and (i == ej):
                b = '#'
            else:
                b = '.'
        a.append(b)
    arr.append(a)
    oj -= 1
    ej += 1
for i in range(row):
    for j in range(col):
        print(arr[i][j], end = "")
    print()