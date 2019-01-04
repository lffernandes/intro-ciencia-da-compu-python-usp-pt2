def encontra_impares(lista,n=None,l_imp=None):

  if n == None:
    n = len(lista)-1
    
  if l_imp==None:
    l_imp=[]
    
  if n < 0:
    return l_imp

  if lista[n] % 2 != 0:
    l_imp.append(lista[n])
    return encontra_impares(lista, n-1, l_imp)

  else:
    return encontra_impares(lista, n-1, l_imp)
                              
    
  
