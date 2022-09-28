from matplotlib import pyplot as plt

def linearApproximation(X, Y):
    x = 0
    y = 0
    x2 = 0
    xy = 0
    n = len(X)
    for i in range(n):
        x += X[i]
        y += Y[i]
        x2 += X[i]*X[i]
        xy += X[i]*Y[i]
    a = (xy - x*(y/n))/(21 - x*x/4)
    b = (y - x*a)/n
    print("{:.3f}x + {:.3f}".format(a, b))
    newY = [(a*X[i] + b) for i in range(n)]
    plt.plot(X, newY)
    plt.scatter(X, Y)
    plt.grid()
    plt.show()

def main():
    X = [0,1,2,4,8,16, 17]
    Y = [0.2, 0.9, 2.1, 3.7, 4.9, 2, 1]
    linearApproximation(X, Y)

if __name__ == "__main__":
    main()