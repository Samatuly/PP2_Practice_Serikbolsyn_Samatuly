a = (input().split())
def histogram(arr):
    n = 0
    for i in arr:
        arr[n] = int(arr[n])
        m = 0
        while m < arr[n]:
            print("*", end = "")
            m += 1
        print()
        n += 1
histogram(a)