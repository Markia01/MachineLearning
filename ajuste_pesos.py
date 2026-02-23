alpha = 0.05 
w = [9.0, 9.0]
grad= [25,50]
for j in range(2):
    w[j] = w[j] + alpha * grad[j]

print("nuevos pesos w =", w)
