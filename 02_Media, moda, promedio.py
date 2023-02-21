import random

maximo = int(input("Ingresa el valor maximo que tendra la lista: "))
cant = int(input("Ingresa la cantidad de numeros: "))

numeros = []

for i in range(cant):
    numeros.append(random.randrange(0, maximo))
    
numeros.sort()

# Media

if cant % 2 == 0:
    i = int(len(numeros) / 2)
    media = int((numeros[i] + numeros[i - 1])//2)
else:
    i = int(len(numeros) // 2)
    media = numeros[i]
    
print(f"Media: {media}")
    
# Moda

frecuencia = {}

for i in numeros:
    frecuencia.setdefault(i, 0)
    frecuencia[i] += 1

frecuente = max(frecuencia.values())

for i, j in frecuencia.items():
    if j == frecuente:
        moda = i
        
print(f"Moda: {moda}")

# Promedio

promedio = sum(numeros)/len(numeros)
print(f"Promedio: {promedio}")

print(f"Lista de numeros: {numeros}")