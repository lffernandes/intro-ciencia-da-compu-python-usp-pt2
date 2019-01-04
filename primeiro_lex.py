def primeiro_lex(lista):
  menor='~'
  for i in range(len(lista)):          
    if lista[i] < menor:
      menor=lista[i]
  return menor
    
