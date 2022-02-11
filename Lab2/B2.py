a = int(input())
arr = list(map(int, input().split()))
if(len(arr) != a):
    exit()
arr.sort()
n = len(arr)
print(arr[n - 1] * arr[n - 2])