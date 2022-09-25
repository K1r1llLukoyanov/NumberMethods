from math import sin, cos, tan
"""
    Достаточное условие сходимости
    
    Пусть функция f(x) имеет первую производную на отрезке [a, b],
    причем выполнено условие знакопостоянства f(a)*f(b) < 0, а производные f`(x) и f``(x)
    сохраняют знаки на отрезке [a, b].
    
    Тогда можно построить итерационную последовательность
    
    x(n+1) = x(n) - (f(x(n))/f`(x(n))), n=0,1,2...

    сходящаюся к единственному на [a, b] решению уравнению f(x) = 0

    В данном методе процесс итераций состоит в том, что в качестве приближения 
    к корню принимаются значения x0,x1,x2,... точек пересения касательной к графику
    и оси обцисс

    Для точек должно выполняться условие f(x)*f''(x) > 0
"""


def func(x):
    # F(x) = 0
    # функция, возвращающая значение функции tg(0.4*x + 0.4) - x^2
    return tan(0.4*x + 0.4) - x**2

def first_direvative(x):
    # первая производная F'(x) = 0
    return 0.4/(cos(0.4*x + 0.4)**2) - 2*x

def second_direvative(x):
    # вторая производная F"(x) = 0
    return -0.32/((cos(0.4*x + 0.4))**3) - 2


def newton(a, b, e): # функция, вычисляющая корень методом Ньютона
    if(func(a)*func(b) > 0): # если на концах отрезок одинаковый знак фукнции, то корень нельзя найти
        print("f(a) and f(b) should be with different signs\n")
        return
    if(func(b)*second_direvative(b) < 0): # если F(a)*F"(a) < 0
        if(func(a)*second_direvative(a) < 0): # и F(b)*F"(b) < 0
            print("Conditions are not allowed!\n") # то корень нельзя найти
            return
        else: # если F(a)*F"(a) < 0 и F(b)*F"(b) > 0, то меняем местами a и b
            t = b
            b = a
            a = t
    
    while(True):
        print("{:<12} {:<12}".format(a, b))     # выводим значние концов отрезок
        b = b - func(b)/first_direvative(b)     # вычисляем новую точку b
        if(abs(func(b)) < e or abs(a-b) < e):   # если значение меньше погрешности, то
            return b    # возвращаем корень
        

def main():
    a = 1 # левый конец отрезока
    b = 2  # правый конец отрезока
    e = 0.0001 # заданная погрешность
    print("{:<12} {:<12}".format("a", "b"))
    print("\nAnswer: ", newton(a,b,e))

if __name__ == "__main__":
    main()