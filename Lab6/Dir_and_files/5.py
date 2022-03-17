list = []
num = int(input("Write number of items: "))
i = 0
while i < num:
    a = input()
    list.append(a)
    i += 1
with open('5.txt', "w") as file:
        for c in list:
                file.write("%s\n" % c)
content = open('5.txt')
print(content.read())