import math
import numpy as np

def func(x):
    return math.sqrt(2*x**2 + 1)

def trapezoid(a, b, n):
    I = 0
    x = np.linspace(a, b, n)
    l = x[1]-x[0]
    for i in range(0, n-1):
        I += 0.5*(func(x[i]) + func(x[i+1]))*l
    print(I)

def main():
    trapezoid(0, 1, 100)

if __name__ == "__main__":
    main()