import math

from Matrix import Matrix
from solving_methods import jacobi, gauss_seidel, lu_decomposition
from utils import N

if __name__ == '__main__':
    # A
    a1 = 5
    a2 = -1
    a3 = -1
    A = Matrix(N, a1, a2, a3)
    b = [0 for i in range(N)]
    x = [0 for i in range(N)]
    residual_norm = 1e-9
    max_norm = 1e-9
    for i in range(N):
        b[i] = math.sin(i * 3)
    # B
    jacobi(A, b, x, max_norm)
    print()
    gauss_seidel(A, b, x, max_norm)
    print()
    # E
    lu_decomposition(A, b, x)
    print()
    #     C
    a1 = 3
    A = Matrix(N, a1, a2, a3)
    jacobi(A, b, x, max_norm)
    print()
    gauss_seidel(A, b, x, max_norm)
    print()
