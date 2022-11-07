import numpy as np

def mnozenie(A:list[int], B:list[int]):
    wynik = np.zeros((A.shape[0], B.shape[1]))
    for i in range(0, A.shape[0]):
        for j in range(0, B.shape[1]):
            for k in range(0, B.shape[0]):
                wynik[i, j] += A[i, k] * B[k, j]
    return wynik

