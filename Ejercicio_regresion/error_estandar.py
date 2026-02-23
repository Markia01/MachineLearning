import math

def calcular_error_estandar(x, y, a, b):
    n = len(x)
    suma_y_cuadrada = sum(val ** 2 for val in y)
    suma_y = sum(y)
    suma_xy = sum(x[i] * y[i] for i in range(n))
    
    numerador = suma_y_cuadrada - (a * suma_y) - (b * suma_xy)
    denominador = n - 2
    
    return math.sqrt(numerador / denominador)