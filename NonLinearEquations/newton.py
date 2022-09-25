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
    # Функция x^2 - x = 1
    return x**2 - x - 1

def first_direvative(x):
    return 2*x - 1

def second_direvative(x):
    return 2


def newton(a, b, e):
    if(func(a)*func(b) > 0):
        print("f(a) and f(b) should be with different signs\n")
        return
    if(func(a)*second_direvative(a) < 0):
        if(func(b)*second_direvative(b) < 0):
            print("Conditions are not allowed!\n")
            return
    else:
        t = b
        b = a
        a = t
    
    while(True):
        if(func(b)*second_direvative(b) < 0):
            print("Conditions are not allowed!\n")
            return
        print(b) 
        b = b - func(b)/first_direvative(b)
        if(abs(func(b)) < e or abs(a-b) < e):
            return b
        

def main():
    a = 1
    b = 2
    e = 0.0001
    print(newton(a,b,e))

if __name__ == "__main__":
    main()