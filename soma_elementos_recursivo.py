def soma_lista(lista, n=None, soma=0):
  if n == None:
   n = len(lista)-1
   
  if n < 0:
    
    return soma
  
  else:
    return soma_lista(lista, n-1, soma=(soma+lista[n]))
    
  
