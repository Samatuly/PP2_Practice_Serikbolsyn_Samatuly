b = input()
if (" " not in b):
    n = b
    x = input()
else:
    n, x = b.split()
n = int(n)
x = int(x)
arr = []
i = 0
while i < n:
    a = x + (2 * i)
    arr.append(a)
    i += 1
xor = 0
i = 0
while i < n:
    xor = xor ^ arr[i]
    i += 1
print(xor)