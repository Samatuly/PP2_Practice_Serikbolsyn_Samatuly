n, f = map(int, input().split())
i = 2
while i < n:
    if(n % i == 0) or (n > 500) or (f % 2 == 1):
        print("Try next time!")
        break
    if(i == n - 1) and (n % i != 0) and (n <= 500) and (f % 2 == 0):
        print("Good job!")
    i += 1
