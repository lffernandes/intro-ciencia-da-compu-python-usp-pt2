import time
import ordena_lista
import random

class ContaTempos:

  def lista_aleatoria(self, n):
    lista = [random.randrange(1000) for x in range(n)] 
    return lista

  def lista_quase_ordenada(self, n):
    lista = [x for x in range(n)]
    lista[n//2] = -500
    lista[n//10] = -200
    return lista
  def compara(self, n):
    lista1= self.lista_aleatoria(n)
    lista2 = lista1[:]

    o = ordena_lista.ordenador()
    print("Comparando com listas aleatórias")
    antes = time.time()
    o.bolha(lista1)
    depois = time.time()
    print("Bolha demorou,", depois - antes)        
    antes = time.time()
    o.ordena(lista2)
    depois = time.time()
    print("Seleção direta demorou,", depois - antes)

    print("\nComparando com listas quase ordenadas")
    lista3 = self.lista_quase_ordenada(n)
    lista4 = lista3[:]

    O = ordena_lista.ordenador()
    antes = time.time()
    o.bolha_curta(lista3)
    depois = time.time()
    print("Bolha demorou,", depois - antes)
  
    antes = time.time()
    o.ordena(lista4)
    depois = time.time()
    print("Seleção direta demorou,", depois - antes)

