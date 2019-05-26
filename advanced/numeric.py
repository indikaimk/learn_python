class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0}, y:{1}>".format(self.x, self.y)
    
    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)
    
    def __sub__(self, p2):
        return Point(self.x - p2.x, self.y - p2.y)

    def __iadd__(self, p2):
        self.x += p2.x
        self.y += p2.y
        return self
    
    def __mul__(self, p2):
        return Point(self.x * p2.x, self.y * p2.y)
    
    def __floordiv__(self, p2):
        return Point(self.x // p2.x, self.y // p2.y)

    def __truediv__(self, p2):
        return Point(self.x / p2.x, self.y / p2.y)

def main():
    p1 = Point(10, 20)
    p2 = Point(11, 36)
    print(p1, p2)
    print(p1 + p2)
    print(p1 - p2)
    p1 += p2
    print("Inplace addition", p1)
    print("multiplication", p1*p2)
    p3 = p1 // p2
    print("{0}//{1} == {2}".format(p1, p2, p3))
    print(p1/p2)

if __name__ == "__main__":
    main()