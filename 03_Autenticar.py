import getpass

users = {"antonio":"antonios26", "toño":"pass", "admin":"admin"}

while True:
    usuario = input("Ingresa tu usuario: ")
    
    if usuario in users.keys():
        break
    else:
        print("Ese usuario no esta registrado!\nIntenta con otro\n")
        
while True:
    password = getpass.getpass("\nIngresa tu contraseña: ")
    
    if password == users.get(usuario):
        break
    else:
        print("La contraseña es incorrecta!\nIntenta otra vez\n")   
        
print("\nVerificado!")