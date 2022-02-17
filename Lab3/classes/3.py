class Shape():
    def __init__ (self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.width = input()
        self.length = input()
        self.width = int(self.width)
        self.length = int(self.length)
    def area(self):
        print(self.width * self.length)
Rectangle().area()