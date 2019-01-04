import random

def lista_aleatoria(n):
    lista = [random.randrange(1000) for x in range(n)] 
    return lista
   
def ordena(lista): #Algoritmo de seleção direta
    for i in range(0,len(lista) -1):
      minIndex = i
      for j in range (i+1,len(lista)):
        if lista[j] < lista[minIndex]:
          minIndex = j
      if minIndex != i:
        lista[i],lista[minIndex] = lista[minIndex],lista[i]
    return lista
