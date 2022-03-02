def square(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1
x = int(input("Enter a number: "))
a = square(x)
for j in a:
    print(j)