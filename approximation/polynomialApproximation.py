import numpy as np
from matplotlib import pyplot as plt

def polynomial(X, Y, n):
    m = n+1 # n - degree of polynomial, m - number of unknowns
    nx = len(X)
    B = np.array([0 for _ in range(m)], np.float32)
    U = np.array([[0 for _ in range(m)] for __ in range(m)], np.float32)
    for i in range(m):
        for j in range(m):
            for k in range(nx):
                U[i][j] += (X[k])**(2*n - i - j)
        for j in range(nx):
            B[i] += (X[j]**(2-i))*Y[j]
    for i in range(m-1):
        j = i
        while(j < m-1 and U[j][i] == 0):
            j+=1
        for k in range(j+1, m):
            if(U[k][i] == 0):
                continue
            coef = -U[k][i]/U[j][i]
            for l in range(i, m):
                U[k][l] += coef*(U[j][l])
            B[k] += B[j]*coef
        U[i], U[j] = U[j], U[i]
        B[i], B[j] = B[j], B[i]
    
    V = [0 for _ in range(m)]
    for i in range(m-1, -1, -1):
        sum = 0
        for j in range(i, m):
            sum += V[j]*U[i][j]
        V[i] = (B[i] - sum)/U[i][i]

    Xs = np.linspace(X[0], X[nx-1], 1000)
    Ys = []
    for i, x in enumerate(Xs):
        Ys.append(0)
        for j in range(m):
            Ys[i] += V[j]*x**(n-j)
    plt.plot(Xs, Ys)
    plt.scatter(X, Y)
    plt.grid()
    plt.show()

def main():
    X = [-2, -1, 0, 1, 2]
    Y = [6, 2, -1, -2, -1]
    polynomial(X, Y, 2)

if __name__ == "__main__":
    main()