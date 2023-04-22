import math

from Matrix import Matrix

N = 980


def residual(A: Matrix, b, x):
    r = A.multiplyByVec(x)
    for i in range(N):
        r[i] -= b[i]
    return r


def norm(v):
    n = 0
    for i in range(N):
        n += v[i] ** 2
    return math.sqrt(n)
