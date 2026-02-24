import pandas as pd


from pendiente import calcular_pendiente
from ordenada import calcular_ordenada
from ecuacion_recta import calcular_prediccion
from error_estandar import calcular_error_estandar
from correlacion import calcular_r
from determinacion import calcular_r2

def main():
    
    df = pd.read_excel('datos.xlsx')
    
    # conversion de columnas a listas
    x = df['NOMINAS'].tolist()
    y = df['VENTAS'].tolist()
    
    b = calcular_pendiente(x, y)
    a = calcular_ordenada(x, y, b)
    print(f"Pendiente (b): {b}")         
    print(f"Ordenada (a): {a}")           
    
    x_pred = 6
    prediccion = calcular_prediccion(a, b, x_pred)
    print(f"\nEcuación de la recta: y = {a} + {b}x")
    print(f"Pronóstico si la nómina es de 600M (x=6): {prediccion} (Es decir, $325,000)")
    
    error = calcular_error_estandar(x, y, a, b)
    print(f"\nError estándar de estimación: {error:.3f}")
    
    r = calcular_r(x, y)
    print(f"Coeficiente de correlación (r): {r:.2f}")
    
    r2 = calcular_r2(r)
    print(f"Coeficiente de determinación (r^2): {r2:.4f} ({r2*100:.2f}%)")

if __name__ == "__main__":
    main()