import numpy as np
from matplotlib import pyplot as plt
import math

def sin(x): return np.sin(math.pi*x)

def spline(X, Y):
    M = []
    B = []
    n = len(X)
    H = [0 for _ in range(n)]

    for i in range(1, n):
        H[i-1] = X[i] - X[i-1]

    for i in range(1, n-1):
        M.append([0 for _ in range(3)])
        M[i-1][0] = H[i-1]
        M[i-1][1] = 2*(H[i-1] + H[i])
        M[i-1][2] = H[i]
        B.append(3*(Y[i+1]-Y[i])/(H[i]) - (Y[i]-Y[i-1])/(H[i-1]))

    V = [0 for _ in range(n)]
    U = [0 for _ in range(n)]
    C = [0 for _ in range(n+1)]
    D = [0 for _ in range(n)]
    BB = [0 for _ in range(n)]

    U[0] = -M[0][2]/M[0][1]
    V[0] = B[0]/M[0][1]

    for i in range(1, n-2):
        U[i] = (B[i] - M[i][0]*V[i-1])/(M[i][0]*U[i-1] + M[i][1])
        V[i] = -M[i][2]/(M[i][0]*U[i-1] + M[i][1])

    C[n] = 0
    for i in range(n-1, -1, -1):
        C[i] = C[i+1]*U[i] + V[i]
    C[0] = 0

    for i in range(n-1):
        D[i] = (C[i+1] - C[i])/(3*H[i])
        BB[i] = (B[i+1] - B[i])/(H[i]) - (H[i+1])*(C[i+1] + 2*C[i])/3
    D[n-1] = -C[n-1]/(3*H[n-2])
    BB[n-1] = (Y[n-1] - Y[n-1])/H[n-2] - 2*H[n-2]*C[n-1]/3

    F = [[0 for _ in range(4)] for __ in range(n)]

    for i in range(n):
        coefs = [[0 for _ in range(4)] for j in range(4)]
        coefs[0][0] = 1
        coefs[1][0] = -X[i]
        coefs[1][1] = 1
        mult = [Y[i], B[i], C[i], D[i]]
        for j in range(2, 4):
            coefs[j] = coefs[j-1][:]
            for k in range(j-1, -1, -1):
                coefs[j][k+1] = coefs[j][k]
                coefs[j][k] = 0
            for k in range(j-1, -1, -1):
                coefs[j][k] += -coefs[j-1][k]*X[i]

        final_coefs = [0 for _ in range(4)]

        for j in range(0, 4):
            for k in range(4-j):
                final_coefs[j] += coefs[-(k+1)][j]*mult[j]

        for j in range(4):
            F[i-1][j] = final_coefs[j]
    
    for i in range(n-1):
        xs = np.linspace(X[i], X[i+1], 1000)
        ys = []
        for j in xs:
            ys.append(0)
            for k in range(4):
                ys += (j**k)*F[i][k]
        plt.plot(xs, ys)
    plt.show()

def main():
    X = np.linspace(0, 2, 10)
    Y = sin(X)
    spline(X, Y)

if __name__ == "__main__":
    main()
