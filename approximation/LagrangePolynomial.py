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

def printLagrange(Lk):
    if(len(Lk) == 1):
        print("L_1(x) = {}".format(Lk[0]))
        return
    print("L_{}(x) = {:.2f}*x^{}".format(len(Lk)-1,Lk[len(Lk)-1], len(Lk)-1), end=' ')
    for i in range(len(Lk)-2, 0, -1):
        if(Lk[i] == 0):
            continue
        elif(Lk[i] > 0):
            print("+ {:.2f}*x^{}".format(Lk[i], i), end=' ')
        else:
            print("- {:.2f}*x^{}".format(-Lk[i], i), end=' ')
    if(Lk[0] > 0):
        print("+ {}".format(Lk[0]))
    elif(Lk[0] < 0):
        print("- {}".format(-Lk[0]))

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