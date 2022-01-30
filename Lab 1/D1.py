z = int(input())
x = str(input())
if x == 'k':
    c = int(input())
    z /= 1024
    print(round(z, c))
if x == 'b':
    z *= 1024
    print(z)
