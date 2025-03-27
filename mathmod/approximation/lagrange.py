def lagrange(x, array_x: list, array_y: list):
    """
    Приближение функции методом Лагранжа

    param x: параметр lambda-функции, который в последующем будет точкой, 
    в которой происходит вычисление функции
    param array_x: массив значений x
    param array_y: массив значений y

    return: 
        L_n - многочлен Лагранжа
    """
    L_n = 0
    for j in range(len(array_x)):
        l_nj = 1
        for k in range(len(array_x)):
            if j != k:
                l_nj *= (x - array_x[k]) / (array_x[j] - array_x[k]) 
        L_n += array_y[j] * l_nj
    return L_n
