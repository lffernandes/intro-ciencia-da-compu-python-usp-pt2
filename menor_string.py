def ordenada(lista):
  menor = float("inf")
  listaordenada=False
  for i in range (len(lista)):  
    if i > menor:
      listaordenada=True
    else:
      listaordenada=False

  return listaordenada
