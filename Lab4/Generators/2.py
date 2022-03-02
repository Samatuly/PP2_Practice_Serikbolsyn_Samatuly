def even(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1
x = int(input())
a = even(x)
for j in a:
    print(j)