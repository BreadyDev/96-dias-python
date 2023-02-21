import random

cant = int(input("Ingresa la cantidad de numeros"))
numeros = []

for i in range(cant):
    numeros.append(random.randrange(0, 20))
    
print(numeros)
numeros.sort()
print(numeros)