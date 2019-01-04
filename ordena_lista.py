
class ordenador:

  def ordena(self, lista): #Algoritmo de seleção direta
    for i in range(0,len(lista) -1):
      minIndex = i
      for j in range (i+1,len(lista)):
        if lista[j] < lista[minIndex]:
          minIndex = j
      if minIndex != i:
        lista[i],lista[minIndex] = lista[minIndex],lista[i]
    return lista


  def bolha(self, lista): #Algoritmo de seleção Bubblesort
    fim = len(lista)

    for i in range(fim-1,0,-1):
      for j in range(i):
        if lista[j] > lista[j+1]:
          lista[j],lista[j+1] = lista[j+1], lista[j]
          trocou=True
    return lista



  def bolha_curta(self, lista): #Algoritmo de seleção Bubblesort
    fim = len(lista)

    for i in range(fim-1,0,-1):
      trocou=False
      for j in range(i):
        if lista[j] > lista[j+1]:
          lista[j],lista[j+1] = lista[j+1], lista[j]
          trocou=True
      if not trocou:
        return lista
    return lista

  
  
