from copy import copy, deepcopy

def printMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=' ')
        print()
    print()

def Det(M): # Находим определитель матрицы
    n = len(M) # размер текущей матрицы
    if(n == 1): # если размер 1x1 возвращаем единственный элемент
        return M[0][0]
    elif(n == 2): # если размер 2x2
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]

    # остальные матрицы считаем с помощью разбиения их на более мелкие

    result = 0 # результат
    koef = 1 # коэф (-1 или 1) в зависимости от номера элемента

    for i in range(n): # построим алгебраические дополнения вокруг элементов первой строки
        NM = [[0 for _ in range(n-1)] for __ in range(n-1)] # создаем новую матрицу
        # и переносим в нее все элементы начальной матрицы, кроме тех, что лежат на первой строке или на i-ой колонне
        # получается матрица (n-1)x(n-1)
        for j in range(1, n): 
            for k in range(n):
                if(k < i):
                    NM[j-1][k] = M[j][k]
                elif(k == i):
                    continue
                else:
                    NM[j-1][k-1] = M[j][k]
        result += koef*Det(NM)*M[0][i] # умножаем элемент на его алгебраическое дополнение и прибавляем к результату
        koef*=(-1) # меняем коэффициент

    return result  # возвращаем определитель матрицы M

def Kramer(A, B):   # Метод крамера
    g = Det(A)      # определитель матрицы A
    dets = [0 for _ in range(len(A[0]))] # пределители матрицы A с заменой столбцов
    for i in range(len(A[0])):
        M = deepcopy(A)         # создаем копию матрицы A
        for j in range(len(A)): # заменяем в ней i-ый столбец матрицей B
            M[j][i] = B[j]
        dets[i] = Det(M)        # записываем в dets[i] определитель полученной матрицы
    for i in range(len(dets)):  # делим определители полученные из матриц с замененными столбцами на определитель матрицы A и получаем ответ
        print(dets[i]/g)

def main():
    A = [   [0.3, 0.2, 0.1, 0.4], 
            [0.3, 2.7, 0.1, 0.2],
            [0.1, 0.2, 2.9, 0.3], 
            [0.1, 0.2, 0.2, 3.1]
        ]
    B = [   0.1, 
            0.2, 
            0.5, 
            0.8
        ]
    
    Kramer(A, B)

if __name__ == "__main__":
    main()