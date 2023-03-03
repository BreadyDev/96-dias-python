def faltante(numeros:list):
    faltantes = []
    for i in range(1, numeros[-1]):
        if i not in numeros:
            faltantes.append(i)
            
    return(faltantes)
    
numeros = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(faltante(numeros))