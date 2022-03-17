mytuple = ()
num = int(input("Please, write number of items in tuple: "))
l = list(mytuple)
i = 0
while i < num:
    a = input()
    l.append(a)
    i += 1
print(all(tuple(l)))