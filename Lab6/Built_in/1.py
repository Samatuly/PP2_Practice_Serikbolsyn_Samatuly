import math
list = input("Enter the numbers: ").split(" ")
i = 0
while i < len(list):
    list[i] = int(list[i])
    i += 1
list = math.prod(list)
print(list)