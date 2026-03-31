import math
class Vector:
    def __init__(self, *args):
        if isinstance(args[0], Vector):
            self.A = args[0].A
        else:
            self.A = args[0]
    def dim(self):
        return len(self.A)
    def length(self):
        quadratic = 0
        for i in range(len(self.A)):
            quadratic += self.A[i] * self.A[i]
        return math.sqrt(quadratic)
    def average(self):
        sum = 0
        for i in range(len(self.A)):
            sum += self.A[i]
        return sum / len(self.A)
    def min(self):
        return min(self.A)
    def max(self):
        return max(self.A)
    def __str__(self):
        return f"Vector{self.A}"

def read(fname):
    with open(fname) as f:
        A = []
        for line in f:
            B = line.split()
            for j in range(len(B)):
                B[j] = float(B[j])
            t = Vector(B)
            A.append(t)
    return A
if __name__ =="__main__":
    A = read("example")
    max_dim_and_min_len = A[0]
    min_dim_and_max_len = A[0]
    max_component = A[0]
    min_component = A[0]
    average = 0
    big = 0
    for el in A:
        if el.dim() > max_dim_and_min_len.dim():
            max_dim_and_min_len = el
        if el.dim() == max_dim_and_min_len.dim():
            if el.length() < max_dim_and_min_len.length():
                max_dim_and_min_len = el
        if el.dim() < min_dim_and_max_len.dim():
            min_dim_and_max_len = el
        if el.dim() == min_dim_and_max_len.dim():
            if el.length() > min_dim_and_max_len.length():
                min_dim_and_max_len = el
        average += el.length()
        if max(max_component.A) < max(el.A):
            max_component = el
        if max(max_component.A) == max(el.A):
            if min(max_component.A) > min(el.A):
                max_component = el
        if min(min_component.A) > min(el.A):
            min_component = el
        if min(min_component.A) == min(el.A):
            if max(max_component.A) < max(el.A):
                max_component = el
    average = average / len(A)
    for el in A:
        if el.length() > average:
            big += 1
    print("max dim and min length:",max_dim_and_min_len)
    print("min dim and max length:", min_dim_and_max_len)
    print("average length:", average)
    print("vectors biggest average length", big)
    print("vector with bigger component:", max_component)
    print("vector with smaller component:", min_component)




