from datetime import date
from datetime import datetime

def calcular_edad(nom, a, m, d):
    nac = date(a, m, d)
    now = datetime.now().date()
    dif_a = int((now - nac).days//365.25)
    dif_d = int((now - nac).days%365.25)
    print(f"{nom}, su fecha de nacimiento es: {nac}\nEdad: {dif_a} años con {dif_d} dias\n")
    
    
fechas = [["Antonio Ramos", 2002, 7, 26], ["Pablo Briones", 2002, 11, 20], ["Raul Mendez", 2002, 6, 19]]

for nom in fechas:
    calcular_edad(nom[0], nom[1], nom[2], nom[3])