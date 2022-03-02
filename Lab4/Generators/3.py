n = int(input())
class numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(self.a <= n):
            x = self.a
            self.a += 1
            if((self.a - 1) % 3 == 0) and ((self.a - 1) % 4 == 0):
                print(x)
        else:
            raise StopIteration
class34 = numbers()
divby3and4 = iter(class34)
for i in divby3and4:
    if(i != None):
        print(i)