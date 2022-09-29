import math
import numpy as np

def func(x):
    return math.sqrt(2*x**2 + 1)

def rectagular(a, b, n):
    I = 0
    x = np.linspace(a, b, n)
    l = x[1] - x[0] 
    for i in range(0, n-1):
        I += l*func(x[i])
    print(I)

def main():
    rectagular(0, 1, 1000)

if __name__ == "__main__":
    main()