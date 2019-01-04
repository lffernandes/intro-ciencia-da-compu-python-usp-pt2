def ordenada(lista):
  menor = 0
  listaordenada=False
  for i in range (len(lista)):  
    if lista[i] >= menor:
      menor=lista[i]
      listaordenada=True
    else:
      return False
  return True
