import random


class Matrix:

    def __init__(self, n, m):
        self.n = n  # строки
        self.m = m  # столбцы
        self.data = [[i + j * random.randint(2, 9) for j in range(1, m + 1)] for i in range(1, n + 1)]

    def value_matrix(self, matrix):
        if self.n == matrix.n and self.m == matrix.m:
            return True
        return False

    def __add__(self, matrix):
        if self.value_matrix(matrix):
            new_matrix = [[self.data[j][i] + matrix.data[j][i] for i in range(self.m)] for j in range(self.n)]
            m1 = Matrix(self.n, self.m)
            m1.data = new_matrix
            return m1

    def __sub__(self, matrix):
        if self.value_matrix(matrix):
            new_matrix = [[self.data[j][i] - matrix.data[j][i] for i in range(self.m)] for j in range(self.n)]
            m1 = Matrix(self.n, self.m)
            m1.data = new_matrix
            return m1

    def __mul__(self, matrix):
        if self.m == matrix.n:
            new_matrix = [[self.compute_c(matrix, i, j) for j in range(matrix.m)] for i in range(self.n)]
            m1 = Matrix(self.n, matrix.m)
            m1.data = new_matrix
            return m1

    def compute_c(self, matrix, i, j):
        total = 0
        for k in range(self.m):
            res = self.data[i][k] * matrix.data[k][j]
            total += res
        return total

    def transposition(self):
        new_matrix = [[self.data[i][j] for i in range(self.m)] for j in range(self.n)]
        m1 = Matrix(self.m, self.n)
        m1.data = new_matrix
        return m1

    def __str__(self):
        str = ""
        for i in range(self.n):
            for j in range(self.m):
                str += f"{self.data[i][j]} "
            str += '\n'
        return str


print("Матрица 1")
m1 = Matrix(3, 3)
print(m1)
print()
print("Матрица 2")
m2 = Matrix(3, 3)
print(m2)
print()
print("Сложение матриц: ")
print(m1 + m2)
print()
print("Вычитание матриц: ")
print(m1 - m2)
print()
print("Матрица 3")
m3 = Matrix(3, 2)
print(m3)
print()
print("Умножение матриц: ")
print(m1 * m3)
print()
print("Транспонирование матрицы: ")
new_m1 = m1.transposition()
print(new_m1)
