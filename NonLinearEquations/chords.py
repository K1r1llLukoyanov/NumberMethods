from math import sin, tan
from numpy import sign

def func(x):
    #   функция F(x) = 0
    #   2*sin(x-0.6) + x - 1.5 = 0 
    return 2*sin(x - 0.6) + x - 1.5

def chords(a, b, e): # метод хорд
    if(func(a)*func(b) > 0): # если значения функции на концах одного знака
        print("func(a) and func(b) should be with different signs")
        return
    count = 0 
    while(True):
        count+=1
        print("{:<12}\t\t{:<12}".format(a, b))          # левый и правый концы
        x0 = a + abs(b-a)/(1 + abs(func(a)/func(b)))    # вычисляем новую точку
        if(abs(func(x0)) < e or abs(a-b) < e):          # если значение в её точке меньше погрешности
            print(count)
            return x0                                   # возвращаем корень
        if(sign(func(a)) == sign(func(x0))):            # если F(a) и F(x0) одного знака
            a = x0                                      # то a = x0
        else:
            b = x0                                      # иначе b = x0

def main():
    a = -1
    b = 5
    e = 0.0001
    x0 = None
    print("Function: x^3 - x - 1 = 0\n")
    print("{:<12}\t\t{:<12}\n".format("a", "b"))
    x0 = chords(a, b, e)
    if(x0 != None):
        print("\nAnswer: x0 = ", x0)

if __name__ == "__main__":
    main()
