def func(n):
    mx = 0
    index = 0
    for i in range(len(n)):
        if i > mx:
            break
        mx = max(int(n[i]) + i, mx)
    if mx >= len(n) - 1:
        return 1
    return 0
print(func(input().split()))