import copy
import time

from Matrix import Matrix
from utils import residual, norm, N


def jacobi(A: Matrix, b, x, max_norm):
    iterations = 0
    x_prev = [1 for i in range(N)]
    start = time.time()
    while True:
        for i in range(N):
            S = 0
            for j in range(N):
                if j != i:
                    S += A.A[i][j] * x_prev[j]
            x[i] = (b[i] - S) / A.A[i][i]
        for i in range(N):
            x_prev[i] = x[i]
        iterations += 1
        r = residual(A, b, x)
        n = norm(r)
        if n <= max_norm:
            break
    end = time.time()
    difference = end - start
    print("Jacobi")
    print(f"Ilość iteracji - {iterations}")
    print(f"Czas trwania - {difference * 1000} ms")
    print(f"Norma rezydualna - {n}")


def gauss_seidel(A: Matrix, b, x, max_norm):
    iterations = 0
    r = [0 for i in range(N)]
    x_prev = [1 for i in range(N)]
    start = time.time()

    while True:
        for i in range(N):
            S = 0
            for j in range(i):
                S += A.A[i][j] * x[j]
            for j in range(i + 1, N):
                S += A.A[i][j] * x_prev[j]
            x[i] = (b[i] - S) / A.A[i][i]
        for i in range(N):
            x_prev[i] = x[i]
        iterations += 1
        r = residual(A, b, x)
        n = norm(r)
        if n <= max_norm:
            break
    end = time.time()
    difference = end - start
    print("Gauss-Seidel")
    print(f"Ilość iteracji - {iterations}")
    print(f"Czas trwania - {difference * 1000} ms")
    print(f"Norma rezydualna - {n}")


def lu_decomposition(A: Matrix, b, x):
    U = copy.deepcopy(A)
    L = Matrix(N, 1, 0, 0)
    start = time.time()
    for i in range(N - 1):
        for j in range(i + 1, N):
            L.A[j][i] = U.A[j][i] / U.A[i][i]
            for k in range(i, N):
                U.A[j][k] = U.A[j][k] - L.A[j][i] * U.A[i][k]
    y = [0 for i in range(N)]
    for i in range(N):
        S = 0
        for j in range(i):
            S += L.A[i][j] * y[j]
        y[i] = (b[i] - S) / L.A[i][i]
    for i in range(N - 1, -1, -1):
        S = 0
        for j in range(i + 1, N):
            S += U.A[i][j] * x[j]
        x[i] = (y[i] - S) / U.A[i][i]
    end = time.time()
    difference = end - start
    r = residual(A, b, x)
    n = norm(r)
    print("Faktoryzacja LU")
    print(f"Czas trwania - {difference * 1000} ms")
    print(f"Norma rezydualna - {n}")
