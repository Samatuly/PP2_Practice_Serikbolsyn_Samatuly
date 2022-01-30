a = str(input())
arr = a.split()
i = 0
while i < len(arr):
    if(len(arr[i]) >= 3):
        print(arr[i], end = " ")
    i += 1
        
