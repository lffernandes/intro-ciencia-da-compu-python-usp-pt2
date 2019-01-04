def menor_nome(lista_de_nomes):
  curto='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
  a='a'
  for i in range(len(lista_de_nomes)):
    a=lista_de_nomes[i]
    a=a.strip().capitalize()
    if len(a) < len(curto):
      curto=a
  return curto
