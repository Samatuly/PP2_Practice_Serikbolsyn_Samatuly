a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
def squares(n, k):
    for i in range(n, k):
        yield i**2
x = squares(a, b)
for j in x:
    print(j)