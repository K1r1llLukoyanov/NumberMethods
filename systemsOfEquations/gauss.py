import random


def gauss(A, B):
    X = [0 for _ in range(len(A[0]))]
    for i in range(len(A)-1):
        j = i
        while (j < len(A) and A[j][i] == 0):
            j += 1
        if (j == len(A)):
            continue
        for k in range(j+1, len(A)):
            if (A[k][i] == 0):
                continue
            coef = -A[k][i]/A[j][i]
            for l in range(i, len(A[0])):
                A[k][l] += A[j][l]*coef
            B[k] += coef*B[j]
    for i in range(len(A)-1, -1, -1):
        if (A[i][i] == 0):
            X[i] = random.randint(5, 10)
            continue
        else:
            Y = 0
            for j in range(i+1, len(A)):
                Y += A[i][j]*X[j]
            X[i] = (B[i] - Y)/A[i][i]
    return X


def main():
    A = [[1, 4, 3], [2, 1, -1], [3, -1, 1]]
    B = [10, -1, 11]
    X = gauss(A, B)
    for i, v in enumerate(X):
        print("x{}) {}".format(i+1, v))
        # x1) 2
        # x2) -1
        # x3) 4
if __name__ == "__main__":
    main()
