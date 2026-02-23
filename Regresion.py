#Datos
x= [1.50,1.60,1.70,1.80,1.90] ##alturas 
y= [53,55,66,76,81]    #pesos 
n= len(x)

#Calcular sumatorias 
sum_x= sum(x)
sum_y= sum(y)
sum_xy= sum(x[i]*y[i] for i in range(n))  
sum_x2= sum(i**2 for i in x)


#calcular pendiente (m)
m= (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)

#calcular intercepto (b)
b = (sum_y - m*sum_x) / n

print("pendiente m=", m)
print("intercepto b=", b)

#prediccion 
altura_nueva= 1.85
peso_predicho= m*altura_nueva + b

print("El peso estimado para la altura ", altura_nueva, "es:", peso_predicho)