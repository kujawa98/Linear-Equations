class Matrix:
    def __init__(self, N, a1, a2, a3):
        self.A = [[0 for i in range(N)] for j in range(N)]
        self.size = N
        for i in range(N):
            for j in range(N):
                if i == j:
                    self.A[i][j] = a1
                elif j == i - 1 or j == i + 1:
                    self.A[i][j] = a2
                elif j == i - 2 or j == i + 2:
                    self.A[i][j] = a3

    def fromOther(self, otherMatrix):
        self.size = otherMatrix.size
        newN = otherMatrix.size
        self.A = [[0 for i in range(newN)] for j in range(newN)]
        for i in range(newN):
            for j in range(newN):
                self.A[i][j] = otherMatrix.A[i][j]

    def multiplyByVec(self, vec):
        N = self.size
        u = [0 for i in range(N)]
        for i in range(N):
            S = 0
            for j in range(N):
                S += self.A[i][j] * vec[j]
            u[i] = S
        return u
