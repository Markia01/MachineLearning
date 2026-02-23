def calcular_pendiente(x, y):
    n = len(x)
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(x[i] * y[i] for i in range(n))
    suma_x_cuadrada = sum(x[i] ** 2 for i in range(n))
    
    media_x = suma_x / n
    media_y = suma_y / n
    
    # Fórmula de la pendiente vista en el video
    numerador = suma_xy - (n * media_x * media_y)
    denominador = suma_x_cuadrada - (n * (media_x ** 2))
    
    return numerador / denominador