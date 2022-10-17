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
            if X[i] == X[j]:
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
            final_koefs[j] += round(Y[i]*koefs[i][j], 3)
        

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
    elif(L[len(L)-1] != 0):
        if(L[len(L)-1] > 0):
            print("{:.3f}*x^{}".format(L[len(L)-1], len(L)-1), end=' ')
        else:
            print("{:.3f}*x^{}".format(-L[len(L)-1], len(L)-1), end=' ')
    for i in range(len(L)-2, 0, -1):
        if (L[i] == 0):
            continue
        elif (L[i] > 0):
            if L[i] == 1:
                print("+ x^{}".format(i), end=' ')
            else:
                print("+ {:.3f}*x^{}".format(L[i], i), end=' ')
        else:
            if (L[i] == -1):
                print("- x^{}".format(i), end=' ')
            else:
                print("- {:.3f}*x^{}".format(-L[i], i), end=' ')
    if (L[0] > 0):
        print("+ {}".format(L[0]))
    elif (L[0] < 0):
        print("- {}".format(-L[0])) 

def main():
    X = [-0.16, 74.48, 4.81, 42.16, 29.72, -71.1, 86.9, 10.4, 12.5, 50.1, 64.1, 86.7, 10.4, -12.5, 60.1, 54.1, 76.7, 10.4, 12.5, 50.1, 71.1, 76.9, 20.4, 12.5, 50.1] 
    Y = [1.13, 14.11, 45.8, 43.62, 92.05, -19.4, 181.0, 13.1, 20.9, -11.8, 14.4, 18.0, 13.1, 19.9, 11.8, 34.4, 28.0, 13.1, 19.9, 11.8, 19.4, 81.0, 23.1, 10.9, 11.8]
    Lk = lagrange(X, Y)
    if(len(Lk) == 0):
        print("Unable to find Lagrange polinomial")
        return
    printLagrange(Lk)
    print(Lk)

if __name__ == "__main__":
    main()