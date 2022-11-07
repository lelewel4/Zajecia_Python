def iloczyn(skalar1:list[int], skalar2:list[int]):
    suma = 0
    for i, a in enumerate(skalar1):
            suma += skalar1[i]*skalar2[i]
    return suma
