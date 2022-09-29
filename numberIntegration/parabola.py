import math
import numpy as np


def func(x):
    return math.sqrt(2*x**2 + 1)


def simpson(a, b, n):
    I = 0
    x = np.linspace(a, b, 2*n)
    l = x[1] - x[0]
    for i in range(0, n-1):
        I += (func(x[2*i]) + 4*func(x[2*i+1]) + func(x[2*i+2]))
    I*=(l/3)
    print(I)

def main():
    simpson(0, 1, 1000)

if __name__ == "__main__":
    main()
