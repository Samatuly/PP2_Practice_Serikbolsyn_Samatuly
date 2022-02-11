import math

x, y = map(int, input().split())
n = int(input())
arr = []
for i in range(n):
    c = []
    a, b = map(int, input().split())
    k1 = pow((a - x), 2)
    k2 = pow((b - y), 2)
    d = (math.sqrt(k1 + k2))
    c.append(a)
    c.append(b)
    c.append(d)
    arr.append(c)
arr.sort(key = lambda x: x[2])
for k in arr:
    k.pop(2)
for j in arr:
    print(*j, end = " ")
    print()