import numpy as np

def suma_macierzy(macierz1:list[int], macierz2:list[int]):
    if(macierz1.shape != macierz2.shape):
        print("Rozne rozmiary macierzy")
        return
    suma = np.zeros(macierz1.shape)
    for i, a in enumerate(macierz1):
        for j, b in enumerate(macierz1):
            suma[i,j] = macierz1[i,j] + macierz2[i,j]
    return suma
