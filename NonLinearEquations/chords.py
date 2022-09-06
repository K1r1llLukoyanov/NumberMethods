import math

def func(x):
    #function f(x) = 0
    return x*x*x - x - 1

def chords(a, b, e):
    if(func(a)*func(b) > 0):
        print("func(a) and func(b) should be with different signs")
        return
    if(func(a) > 0):
        t = a
        a = b
        b = t

    while(func(a) < func(b)):
        print("{:<12}\t\t{:<12}".format(a, b))
        x0 = a + (b-a)/(1 + abs(func(a)/func(b)))
        if(abs(func(x0)) < e):
            return x0
        if(func(x0) < 0):
            a = x0
        else:
            b = x0

def main():
    a = 1
    b = 2
    e = 0.0001
    x0 = None
    print("Function: x^3 - x - 1 = 0\n")
    print("{:<12}\t\t{:<12}\n".format("left", "right"))
    x0 = chords(a, b, e)
    if(x0 != None):
        print("\nAnswer: x0 = ", x0)

if __name__ == "__main__":
    main()
