from matplotlib import pyplot as plt
import numpy as np
import math

fig, (ax0, ax1, ax2) = plt.subplots(3, 1)   # функция создает окно, на котором будут
                                            # 3 графика для разных регрессий.

def standart_error(X, Y): # функция для вычисления стандартной ошибки
    x = 0   # сумма всех x
    y = 0   # сумма всех y
    n = len(X)
    for i in range(n):
        x += X[i]
        y += Y[i]
    xavg = x/2  # среднее значение x
    yavg = y/2  # среднее значение y
    qx = 0      # стандартное отклонение
    qy = 0      # стандартное отклонение
    for i in range(n):
        qx += (X[i] - xavg)**2
        qy += (Y[i] - yavg)**2
    qx = math.sqrt(qx/(n-1))/math.sqrt(n)    # стандартная ошибка x
    qy = math.sqrt(qy/(n-1))/math.sqrt(n)    # стандартная ошибка y
    
    return (qx, qy) # возвращение стандартных ошибок

def R2(X, Y, a0, a1): # коэф. детерминации для линеной регрессии
    SSE = 0     # сумма квадратов остатков регрессии
    SST = 0     # общая сумма квадратов
    y = 0
    for i in range(len(Y)):
        y = Y[i]
    yavg = y/2  # среднее значение y
    for i in range(len(X)):
        SSE += (Y[i] - (a0 + a1*X[i]))**2
        SST += (Y[i] - yavg)**2
    
    return 1 - SSE/SST # коэффициент детерминации

def R2E(X, Y, a0, a1): # коэффициент детерминации для экспоненциальной регрессии
    SSE = 0     # сумма квадратов остатков регрессии
    SST = 0     # общая сумма квадратов
    y = 0
    for i in range(len(Y)):
        y = Y[i]
    yavg = y/2  # среднее значение y
    for i in range(len(X)):
        SSE += (Y[i] - math.e**(a0 + a1*X[i]))**2
        SST += (Y[i] - yavg)**2
    
    return 1 - SSE/SST # коэффициент детерминации

def R2P(X, Y, coef): # коэффициент детерминации для полиномиальной регрессии
    SSE = 0     # сумма квадратов остатков регрессии
    SST = 0     # общая сумма квадратов
    y = 0
    for i in range(len(Y)):
        y = Y[i]
    yavg = y/2  # среднее значение y
    for i in range(len(X)):
        yT = 0
        for j in range(len(coef)):
            yT += coef[j]*X[i]**(len(coef) - j - 1)     # предсказанное значение y.
        SSE += (Y[i] - yT)**2
        SST += (Y[i] - yavg)**2
    
    return 1 - SSE/SST # коэффициент детерминации

def linearRegression(X, Y): # линейная регрессия
    x = 0
    y = 0
    x2 = 0
    xy = 0
    n = len(X)
    for i in range(n):
        x += X[i]       #сумма всех иксов
        y += Y[i]       #сумма всех игреков
        x2 += X[i]*X[i] #сумма квадратов всех иксов
        xy += X[i]*Y[i] #сумма произведений x_i*y_i
    a1 = (xy - x*(y/n))/(21 - x*x/4)    # значение коэффициента a1
    a0 = (y - x*a1)/n                   # значение коэффициента a0
    print("Linear:")
    print("a0 = {:.3f}, a1 = {:.3f}".format(a0, a1))
    print("f(x) = {:.3f}x + {:.3f}".format(a1, a0))
    newY = [(a1*X[i] + a0) for i in range(n)]
    print("R^2 = {}".format(R2(X, Y, a0, a1)))
    print("R = {}".format(math.sqrt(R2(X, Y, a0, a1))))
    se = standart_error(X, newY)
    print("standart error y: {}".format(se[1]))
    print("standart error x: {}".format(se[0]))
    ax0.plot(X, newY)   # выводим на первый график функцию прямой регрессии(plot выводит график кривой).
    ax0.scatter(X, Y)   # выводим точки начальных данных.(scatter просто отрисовывает точки). 
    ax0.grid()          # добавление сетки на график
    ax0.set_title('Линейная регрессия') # добавление заголовка к графику

def ExponentialRegression(X, Y):    # экспоненциальная регрессия
    fit = np.polyfit (X, np.log (Y), 1) # функция библеотеки numpy.
    print("\nExponential:")
    print("a0 = {:.3f}, a1 = {:.3f}".format(fit[1], fit[0])) # вывод коэффициентов
    print("f(x) = e^(x*{:.3f}+{:.3f})".format(fit[0], fit[1]))
    Xs = np.linspace(min(X), max(X), 1000)
    NEWY = []
    for i in range(len(Xs)):
        NEWY.append(math.e**(fit[0]*Xs[i] + fit[1])) # вычисление предсказанных y.
    se = standart_error(X, NEWY)
    print("R^2 = {}".format(R2E(X, Y, fit[1], fit[0]))) # вывод коэффициента детерминации
    print("R = {}".format(math.sqrt(R2E(X, Y, fit[1], fit[0]))))
    print("standart error y: {}".format(se[1]))
    print("standart error x: {}".format(se[0]))
    ax1.plot(Xs, NEWY)   # выводим на второй график функцию экспоненциальной регрессии
    ax1.scatter(X, Y)   # выводим точки начальных данных
    ax1.grid()          # добавление сетки на график
    ax1.set_title('Экспоненциальная регрессия') # добавление заголовка к графику

def PolynomialRegression(X, Y, n): # полиномиальная регрессия
    m = n+1 # n - степень полинома, m - количество нужных коэффициентов
    nx = len(X)
    B = np.array([0 for _ in range(m)], np.float32) # Свободные коэффициенты
    U = np.array([[0 for _ in range(m)] for __ in range(m)], np.float32) # матричные коэффициенты
    
    # Расчет коэффициентов полиномиальной регрессии с помощью системы уравнений,
    # решаемой методом Гаусса
    for i in range(m):
        for j in range(m):
            for k in range(nx):
                U[i][j] += (X[k])**(2*n - i - j) # вычисление матричных коэффициентов. 
        for j in range(nx):
            B[i] += (X[j]**(n-i))*Y[j] # вычисление свободных коэффициентов.
    # приведение матрицы к ступенчатому виду
    for i in range(m-1):
        j = i
        while(j < m-1 and U[j][i] == 0): # поиск первой ненулевой строки начиная с i-ой строки в i-ом столбце
            j+=1
        for k in range(j+1, m):
            if(U[k][i] == 0):
                continue
            coef = -U[k][i]/U[j][i] # общий коэффициент для обнуления элемента U[k][i]
            for l in range(i, m):
                U[k][l] += coef*(U[j][l])
            B[k] += B[j]*coef
        if i != j:
            U[i], U[j] = U[j], U[i] # замена строк, если первая ненулевая строка не под номером i.
            B[i], B[j] = B[j], B[i]
    # вычисление коэффициентов начиная с a_n до a_0
    # V[0] = a_n, V[n] = a_0
    V = [0 for _ in range(m)]
    for i in range(m-1, -1, -1):
        sum = 0
        for j in range(i, m):
            sum += V[j]*U[i][j]
        V[i] = (B[i] - sum)/U[i][i]

    Xs = np.linspace(min(X), max(X), 1000) # деление отрезка [min(X), max(X)] на 1000 равных частей.
    Ys = [] # массив для предсказанных y.
    YS = np.zeros(nx)
    for i in range(nx):
        for j in range(m):
            YS[i] += V[j]*X[i]**(n-j)
    for i, x in enumerate(Xs):
        Ys.append(0)
        for j in range(m):
            Ys[i] += V[j]*x**(n-j) # вычисление предсказанных y.
    print("\nPolynomial:")
    for i in range(m):
        print("a{} = {}".format(i, V[(n-i)])) # вывод коэффициентов регрессии
    print("R^2 = {}".format(R2P(X, Y, V))) # вывод коэффициента детерминации
    print("R = {}".format(math.sqrt(R2P(X, Y, V))))
    se = standart_error(X, YS)
    print("standart error y: {}".format(se[1]))
    print("standart error x: {}".format(se[0]))
    ax2.plot(Xs, Ys)    # добавление графика регрессии
    ax2.scatter(X, Y)   # выводy точек начальных данных
    ax2.grid()          # добавление сетки на график
    ax2.set_title('Полиномиальная регрессия, степень={}'.format(n)) # добавление заголовка


def main():
    # начальные данные
    X = np.array([7.6, 7.2, 6.8, 13.4, 20.1, 12.3, 4.5, 4.6, 4.7, 12.5, 20.2, 14.9, 9.9, 12.0])
    Y = np.array([27.2, 20.3, 13.4, 16.5, 19.7, 20.8, 21.9, 20.2, 18.7, 20.9, 23.0, 21.1, 19.0, 23.9])
    linearRegression(X, Y)
    ExponentialRegression(X, Y)
    PolynomialRegression(X, Y, 6)
    plt.show() # вывод графиков на экран

if __name__ == "__main__":
    main()