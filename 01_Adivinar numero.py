import random

print("Adivina un numero entero entre el 0 y el 20!\n")
num = random.randrange(0, 20)
user = -1

while num != user:
    user = int(input("Ingresa un numero: "))
    
    if num > user:
        print("El numero a adivinar es mayor\n")
    elif num < user:
        print("El numero a adivinar es menor\n")
    else:
        break
    
print("Adivinaste!!")