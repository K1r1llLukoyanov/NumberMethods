import math

def runThrough(A, B):
    X = [0 for _ in range(len(A))]
    V = [0 for _ in range(len(A))]
    U = [0 for _ in range(len(A))]

    """
        a_i*x_{i-1} + b_i*x_i + c_i*x_{i+1} = d_i

        x_i = x_{i+1}*U_i + V_i

        x_{i-1} = x_i*U_{i-1} + V_{i-1}

        a_i*(x_i*U_{i-1} + V_{i-1}) + b_i*x_i + c_i*x_{i+1} = d_i
        
        x_i*(a_i*U_{i-1} + b_i) = d_i - c_i*x_{i+1} - a_i*V_{i-1}
        
        x_i = (d_i - c_i*x_{i+1} - a_i*V_{i-1})/(a_i*U_{i-1} + b_i)

        Forward traversal:

        U_i = -c_i/(a*U_{i-1} + b_i)
        
        V_i = (d_i - a_i*V_{i-1})/(a_U{i-1} + b_i)
        
        Backward traversal:
        
        x_i = x_{i+1}*U_i + V_i

    """ 
    
    U[0] = -A[0][2]/A[0][1]
    V[0] = B[0]/A[0][1]

    for i in range(1, len(A)):
        U[i] = -A[i][2]/(A[i][0]*U[i-1] + A[i][1])
        V[i] = (B[i] - A[i][0]*V[i-1])/(A[i][0]*U[i-1] + A[i][1])
    
    X[len(A)-1] = V[len(A)-1]
    
    i = len(A)-2
    
    while(i >= 0):
        X[i] = U[i]*X[i+1] + V[i]
        i-=1
    
    return X

def main():
    A = [[0, 10, 1, 5],[-2, 9, 1, -1],[0.1, 4, -1, -5],[-1, 8, 0, 40]]
    B = [5, -1, -5, 40]
    X = runThrough(A, B)
    for i, v in enumerate(X):
        print("x{}) {}".format(i+1, v))

if __name__ == "__main__":
    main()