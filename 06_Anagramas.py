def anagrama_dict(palabras:list):
    anagrama = {}
    for palabra in palabras:
        sorteada = "".join(sorted(palabra))
        if sorteada in anagrama.keys():
            anagrama[sorteada].append(palabra)
        else:
            anagrama[sorteada] = [palabra]

    return list(anagrama.values())

from collections import defaultdict

def anagrama_defdict(palabras:list):
    anagrama = defaultdict(list)
    
    for palabra in palabras:
        sorteado = "".join(sorted(palabra))
        anagrama[sorteado].append(palabra)
        
    return list(anagrama.values())


palabras = ["tea", "eat", "bat", "ate", "arc", "car"]

print(anagrama_dict(palabras))   

print(anagrama_defdict(palabras))    