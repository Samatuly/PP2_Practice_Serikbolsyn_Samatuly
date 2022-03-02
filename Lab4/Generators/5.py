from re import I


n = int(input("Enter a number: "))
def down(a):
    for i in range(n, 0, -1):
        yield i
x = down(n)
for j in x:
    print(j)