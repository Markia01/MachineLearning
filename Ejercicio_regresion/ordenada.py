def calcular_ordenada(x, y, b):
    n = len(x)
    media_x = sum(x) / n
    media_y = sum(y) / n
    
    # Fórmula: a = promedio_y - b * promedio_x
    return media_y - (b * media_x)