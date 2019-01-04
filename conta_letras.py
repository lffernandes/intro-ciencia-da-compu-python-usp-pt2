def conta_letras(frase,contar="vogais"):
  vogais=('aeiou')
  qtd_vogais=0
  vogal=False
  qtd_consoantes=0
  for i in range(len(frase)):
    for j in range(len(vogais)): 
      if frase[i] != ' ':
        if vogais[j] == frase[i]:
          qtd_vogais+=1
          vogal=True
          break
        else:
          vogal=False    
    if frase[i] != ' ' and not vogal:
      qtd_consoantes+=1
      
  if contar == 'vogais':
    return qtd_vogais
  else:
      return qtd_consoantes
    
