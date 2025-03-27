import numpy as np


def gauss_partial_pivot(a, b):
    n = len(b)
    a = np.copy(a)
    b = np.copy(b)

    for i in range(n):
        # Находим строку с максимальным элементом в i-ом столбце от i до n
        max_row = np.argmax(abs(a[i:, i])) + i
        
        # Меняем местами строки
        if i != max_row:
            a[[i, max_row]] = a[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = a[j, i] / a[i, i]
            a[j, i:] -= factor * a[i, i:]
            b[j] -= factor * b[i]
    
    # Обратный ход для получения решения
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
    
    return x


