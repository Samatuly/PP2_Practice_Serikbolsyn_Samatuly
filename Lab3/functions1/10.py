arr = input().split()
arr.sort()
new_arr = []
def unique(x):
    i = 0
    for j in x:
        if(i == 0):
            new_arr.append(x[i])
        elif(x[i] != x[i - 1]):
            new_arr.append(x[i])
        i += 1
    print(new_arr)
unique(arr)
