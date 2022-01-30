n = int(input())
arr = []
i = 0
while  i < n:
    a = int(input())
    arr.append(a)
    i = i + 1
for x in arr:
    if(x <= 10):
        print("Go to work!")
    if(x > 10) and (x <= 25):
        print("You are weak")
    if(x > 25) and (x <= 45):
        print("Okay, fine")
    if(x > 45):
        print("Burn! Burn! Burn Young!")
