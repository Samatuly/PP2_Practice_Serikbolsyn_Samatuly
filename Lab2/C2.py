arr = []
x = int(input())
row = col = x
for i in range(row):
    a = []
    for j in range(col):
        if(i == j):
            b = pow(i, 2)
        elif(i == 0):
            b = j
        elif(j == 0):
            b = i
        else:
            b = 0
        a.append(b)
    arr.append(a)
for i in range(row):
    for j in range(col):
        print(arr[i][j], end = " ")
    print()