datos=open("Practica2_ml.csv","r")
lineas=datos.readlines()
datos.close()


x=[]
y=[]
lineas =lineas[1:]

for linea in lineas:
    partes=linea.strip("").split(",")
    x.append(float(partes[0]))
    y.append(float(partes[1]))
    
print(x)
print(y)
