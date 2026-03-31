import math

class Triangle:
    @staticmethod
    def check(a, b, c):
        return a + b > c and b + c > a and c + a > b
    def __init__(self, a, b, c, d = None):
        assert Triangle.check(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = (self.a + self.b + self.c) / 2
        s_2 = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s_2 ** 0.5
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"
class Rectangle:
    def __init__(self, a, b, c = None, d = None):
        self.a = a
        self.b = b
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"
class Trapeze:
    @staticmethod
    def check(a, b, c, d):
        return abs(a - b) + c > d and abs(b - a) + d > c and c + d > abs(b - a)
    def __init__(self, a, b, c, d):
        assert Trapeze.check(a, b, c, d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        e = abs(self.a - self.b)
        if e != 0:
            p1 = (e + self.d + self.c)/2
            s1 = (p1 * (p1 - e) * (p1 - self.d) * (p1 - self.c)) ** 0.5
            h1 = 2 * s1 / e
            return h1 * (self.a + self.b)/2
        else:
            return self.a * self.c
    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"
class Parallelogram:
    def __init__(self, a, b, c, d = None):
        self.a = a
        self.b = b
        self.h = c
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.b * self.h
    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"
class Circle:
    def __init__(self, a, b = None, c = None, d = None):
        self.radius = a
    def perimeter(self):
        return 2 * self.radius * math.pi
    def area(self):
        return self.radius * self.radius * math.pi
    def __str__(self):
        return f"Circle({self.radius})"

def read(file: str):
    i = 0
    with open(file) as f:
        for line in f:
            try:
                A = [0] * 5
                B = line.split()
                for k in range(len(B)):
                    if k > 0:
                        A[k] = float(B[k])
                    else:
                        A[k] = B[k]
                if A[0] == "Triangle":
                    t = Triangle(A[1], A[2], A[3], A[4])
                if A[0] == "Rectangle":
                    t = Rectangle(A[1], A[2], A[3], A[4])
                if A[0] == "Trapeze":
                    t = Trapeze(A[1], A[2], A[3], A[4])
                if A[0] == "Parallelogram":
                    t = Parallelogram(A[1], A[2], A[3], A[4])
                if A[0] == "Circle":
                    t = Circle(A[1], A[2], A[3], A[4])
                if i == 0:
                    smax = [t.area(), t]
                    pmax = [t.perimeter(), t]
                    i = i + 1
                else:
                    if smax[0] < t.area():
                        smax = [t.area(), t]
                    if pmax[0] < t.perimeter():
                        pmax = [t.perimeter(), t]
            except AssertionError:
                pass
    return smax, pmax
if __name__ == "__main__":
    A = read("input01.txt")
    print(A[0][1], end="")
    print(" Have bigger area:", A[0][0])
    print(A[1][1], end="")
    print(" Have bigger perimeter:", A[1][0])



