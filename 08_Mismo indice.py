def mismo_indice(lista:list):
    ordenados = []
    for elemento in lista:
        for i in range(len(elemento)):
            try:
                ordenados[i].append(elemento[i])
            except:
                ordenados.append([elemento[i]])
    print(ordenados)
    
from collections import defaultdict
    
def mismo_indice_defdict(lista:list):
    ordenados = defaultdict(list)
    for i, elemento in enumerate(lista):
        ordenados[i].append(elemento)
    print(ordenados.values())
        
elementos = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150, 160]]
mismo_indice(elementos)
mismo_indice_defdict(elementos)