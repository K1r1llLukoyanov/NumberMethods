from math import sin, tan

def func(x):
    #return function f(x) = 0
    return tan(0.4*x + 0.4) - x**2

# finds point x where f(x) = 0
def bisection(a, b, e):
    if(func(a)*func(b) > 0):
        print("func(a) and func(c) should be with different signs\n");
        return
    count = 0
    while(a < b):
        count += 1
        print("{:<12}\t\t{:<12}".format(a, b))
        x0 = a + (b-a)/2
        if(abs(func(x0)) < e):
            print(count)
            return x0
        if(func(x0) < 0):
            if(func(a) < 0):
                a = x0
            else:
                b = x0
        else:
            if(func(b) > 0):
                b = x0
            else:
                a = x0
    
def main():
    a = 1
    b = 2
    e = 0.0001
    x0 = None
    print("Function: x^3 - x - 1 = 0\n")
    print("{:<12}\t\t{:<12}\n".format("left", "right"))
    x0 = bisection(a, b, e)
    if(x0 != None):
        print("\nAnswer: x = ", x0)

if __name__ == "__main__":
    main()
