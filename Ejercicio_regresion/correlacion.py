import math

def calcular_r(x, y):
    n = len(x)
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(x[i] * y[i] for i in range(n))
    suma_x_cuadrada = sum(x[i] ** 2 for i in range(n))
    suma_y_cuadrada = sum(y[i] ** 2 for i in range(n))
    
    numerador = (n * suma_xy) - (suma_x * suma_y)
    denominador_x = (n * suma_x_cuadrada) - (suma_x ** 2)
    denominador_y = (n * suma_y_cuadrada) - (suma_y ** 2)
    
    return numerador / math.sqrt(denominador_x * denominador_y)