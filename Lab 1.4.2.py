class Vector:
    def __init__(self, *args):
        if isinstance(args[0], Vector):
            self.A = args[0].A
        else:
            A = []
            for element in args:
                A.append(float(element))
            self.A = A
    def dim(self):
        return len(self.A)
    def length(self):
        quadratic = 0
        for i in range(len(self.A)):
            quadratic += self.A[i] * self.A[i]
        return math.sqrt(quadratic)
    def __str__(self):
        return f"Vector{self.A}"
class Politangle:
    def __init__(self, *args):
        self.A = args
    @staticmethod
    def _exist(x1, x2, *args):
        A = args[0]
        B = []
        for j in range(1, len(A)):
            B.append([A[j].A[0], A[j].A[1]])
        if x2.A[0] != x1.A[0]:
            something = A[0].A[1] - x1.A[1] - (x2.A[1] - x1.A[1])*(A[0].A[0] - x1.A[0])/(x2.A[0] - x1.A[0])
        else:
            something = x1.A[0] - A[0].A[0]
        if something < 0:
            sgn = "-"
        else:
            sgn = "+"
        for el in B:
            if x2.A[0] != x1.A[0]:
                something = el[1] - x1.A[1] - (x2.A[1] - x1.A[1])*(el[0] - x1.A[0]) / (x2.A[0] - x1.A[0])
            else:
                something = x1.A[0] - el[0]
            if something < 0:
                sgn2 = "-"
            else:
                sgn2 = "+"
            if sgn != sgn2:
                return False
        return True
    def opucly(self):
        B = []
        for i in range(len(self.A)):
            if (i != 0) and (i != len(self.A) - 1):
                B.append(self.A[i])
        if not( Politangle._exist(self.A[0], self.A[ len(self.A) - 1],B) ):
            return False
        for i in range(len(self.A) - 1):
            B = []
            for j in range(len(self.A)):
                if (j != i) and (j != i + 1):
                    B.append(self.A[j])
            if not( Politangle._exist(self.A[i], self.A[i + 1], B) ):
                return False
        return True
def read(filename):
    with open(filename) as f:
        B = []
        for line in f:
            A = line.split()
            B.append(Vector(*A))
    return Politangle(*B)
if __name__ == "__main__":
    print(read("example").opucly())




