string = str(input("Write something: "))
sum_upper = 0
sum_lower = 0
for i in string:
    if(ord(i) >= 65) and (ord(i) <= 90):
        sum_upper += 1
    elif(ord(i) >= 97) and (ord(i) <= 122):
        sum_lower += 1
print(sum_upper)
print(sum_lower)