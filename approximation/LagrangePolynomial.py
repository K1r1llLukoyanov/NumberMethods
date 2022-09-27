""" 
    Langrange polinomial:
    P(x) = L_{n-1}(x) = \sum_{i=1}^n{y_il_i(x)} 
    L_{n-1}(x) = y_1l_1(x) + y_2l_2(x) + ... + y_nl_n(x)
"""

def lagrange(X, Y):
    to_find = []
    for i, v in enumerate(Y):
        if v != 0:
            to_find.append(i)
    koefs = {}
    for i in to_find:
        koefs[i] = [0 for _ in range(len(X))]
        denum = 1
        k = 0
        for j in range(len(X)):
            if i == j:
                continue
            denum *= (X[i] - X[j])
            if(k == 0):
                koefs[i][0] = -X[j]
                koefs[i][1] = 1
            else:
                prevkoefs = koefs[i][:]
                for l in range(k, -1, -1):
                    koefs[i][l+1] = koefs[i][l]
                    koefs[i][l] = 0
                for l in range(k, -1, -1):
                    koefs[i][l] = koefs[i][l] - X[j]*prevkoefs[l]
            k+=1 
        for j in range(len(X)):
            koefs[i][j]/=denum
    
    final_koefs = [0 for _ in range(len(X))]
    for i in to_find:
        for j in range(len(koefs[i])):
            final_koefs[j] += Y[i]*koefs[i][j]

    return final_koefs

def printLagrange(L):
    print("L_{}(x) = ".format(len(L)-1), end = '')
    if (len(L) == 1):
        print(L[0])
        return
    if L[len(L)-1] == 1:
        print("x^{}".format(len(L)-1), end=' ')
    elif(L[len(L)-1] == -1):
        print("-x^{}".format(len(L)-1), end=' ')
    elif(L[0] != 0):
        if(L[0] > 0):
            print("{:.2f}*x^{}".format(L[len(L)-1], len(L)-1), end=' ')
        else:
            print("-{:.2f}*x^{}".format(-L[len(L)-1], len(L)-1), end=' ')
    for i in range(len(L)-2, 0, -1):
        if (L[i] == 0):
            continue
        elif (L[i] > 0):
            if L[i] == 1:
                print("+ x^{}".format(i), end=' ')
            else:
                print("+ {:.2f}*x^{}".format(L[i], i), end=' ')
        else:
            if (L[i] == -1):
                print("- x^{}".format(i), end=' ')
            else:
                print("- {:.2f}*x^{}".format(-L[i], i), end=' ')
    if (L[0] > 0):
        print("+ {}".format(L[0]))
    elif (L[0] < 0):
        print("- {}".format(-L[0])) 

def main():
    X = [-1, 0, 0.5, 1]
    Y = [0, 2, 9/8, 0]
    Lk = lagrange(X, Y)
    if(len(Lk) == 0):
        print("Unable to find Lagrange polinomial")
        return
    printLagrange(Lk)

if __name__ == "__main__":
    main()