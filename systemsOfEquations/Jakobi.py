
def jakobi(A, B, e):
    not_conds = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            if j == i:
                continue
            sum += A[i][j]
        if (abs(sum) > abs(A[i][i])):
            not_conds.append((i, sum))

    for i, s in not_conds:
        for j in range(len(A)):
            if i == j:
                continue
            sum = 0
            for k in range(len(A[j])):
                if k == i:
                    continue
                sum += A[j][k]
            if (abs(A[j][i]) > abs(sum)):
                while abs(A[i][i]) < abs(s):
                    s += sum
                    for h in range(len(A[i])):
                        A[i][h] += A[j][h]
                break

    X = [0 for _ in range(len(A))]

    while 1:
        Xp = X[:]
        for i in range(len(A)):
            b = B[i]
            for j in range(len(A[i])):
                if i == j:
                    continue
                b -= Xp[j]*A[i][j]
            X[i] = b/A[i][i]
        max = abs(X[0] - Xp[0])
        for i in range(1, len(X)):
            if (abs(X[i]-Xp[i]) > max):
                max = abs(X[i] - Xp[i])
        if (max < e):
            break
    return X


def main():
    A = [[7, 4, -1], [2, 6, 3], [-1, 1, 4]]
    B = [7, -2, 4]
    e = 0.0001
    X = jakobi(A, B, e)

    for i, v in enumerate(X):
        print("x{}) {}".format(i+1, v))

    print("Checking result:")

    for i in range(len(A)):
        print(B[i], end=' ')
        result = B[i]
        for j in range(len(A[i])):
            print("- {:.1f}*{}".format(X[j], A[i][j]), end=' ')
            result -= X[j]*A[i][j]
        print("= {:.3f}".format(result))


if __name__ == "__main__":
    main()
