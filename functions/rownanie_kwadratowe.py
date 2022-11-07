import math

def kwadratowe(a:int, b:int, c:int):
    delta = (b*b)-(4*a*c)
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        #print("\nx1 = ", x1 ,"\nx2 = ", x2)
        return float(x1), float(x2)
    if delta == 0:
        x0 = -b / 2*a
        #print("\nx0 = ", x0)
        return float(x0)
    if delta < 0:
        print("Brak miejsc zerowych")

