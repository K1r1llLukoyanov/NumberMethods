"""
    Newton polynomial interpolation:
    N_{n-1}(x) = \Delta^0(x_1)+\Delta^1(x_1, x_2)(x-x_1) + \Delta^2(x-x_1)(x-x_2)+...\\...+\Delta^{n-1}(x_1,x_2,...,x_{n-1})(x-x_1))(x-x_2)...(x-x_{n-1})
    
    where
    
    \Delta^0(x_i) = y_i
    
    \Delta^1(x_i, x_j) = (\Delta^0(x_i) - \Delta^0(x_j))/(x_i - x_j)
    
    \Delta^2(x_i, x_j, x_k) = (\Delta^0(x_i, x_j) - \Delta^0(x_j, x_k))/(x_i - x_k)

    ...
"""


def newton(X, Y):
    n = len(X)
    components = [[0 for _ in range(n-i)] for i in range(n)]
    for i in range(len(X)):
        components[0][i] = Y[i]
    for i in range(1, len(X)):
        for j in range(len(components[i])):
            components[i][j] = (components[i-1][j] -
                                components[i-1][j+1])/(X[j] - X[j+i])

    final_coef = [0 for _ in range(len(X))]
    coefs = {0: [components[0][0]]}

    for i in range(1, len(X)):
        coefs[i] = [0 for _ in range(i+1)]
        for j in range(i):
            if j == 0:
                coefs[i][0] = -X[j]
                coefs[i][1] = 1
            else:
                prev_coefs = coefs[i][:]
                for k in range(j, -1, -1):
                    coefs[i][k+1] = coefs[i][k]
                    coefs[i][k] = 0
                for k in range(j, -1, -1):
                    coefs[i][k] += -X[j]*prev_coefs[k]
        for j in range(i+1):
            coefs[i][j] *= components[i][0]

    final_coef = [0 for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(i, n):
            final_coef[i] += coefs[j][i]

    return final_coef


def print_newton_polynomial(N):
    print("N_{}(x) = ".format(len(N)-1), end='')
    if (len(N) == 1):
        print(N[0])
        return
    if N[len(N)-1] == 1:
        print("x^{}".format(len(N)-1), end=' ')
    elif (N[len(N)-1] == -1):
        print("-x^{}".format(len(N)-1), end=' ')
    elif (N[0] != 0):
        if (N[0] > 0):
            print("{:.2f}*x^{}".format(N[len(N)-1], len(N)-1), end=' ')
        else:
            print("-{:.2f}*x^{}".format(-N[len(N)-1], len(N)-1), end=' ')
    for i in range(len(N)-2, 0, -1):
        if (N[i] == 0):
            continue
        elif (N[i] > 0):
            if N[i] == 1:
                print("+ x^{}".format(i), end=' ')
            else:
                print("+ {:.2f}*x^{}".format(N[i], i), end=' ')
        else:
            if (N[i] == -1):
                print("- x^{}".format(i), end=' ')
            else:
                print("- {:.2f}*x^{}".format(-N[i], i), end=' ')
    if (N[0] > 0):
        print("+ {}".format(N[0]))
    elif (N[0] < 0):
        print("- {}".format(-N[0]))


def main():
    X = [-1, 0, 0.5, 1]
    Y = [0, 2, 9/8, 0]
    newton_coefs = newton(X, Y)
    print_newton_polynomial(newton_coefs)


if __name__ == "__main__":
    main()
