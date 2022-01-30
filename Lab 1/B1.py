sum = 0
x = (input())
for a in x:
    sum += ord(a)
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")
