def compara_matriz(mt1,mt2):
  linmt1=colmt1=0
  for i in range(len(mt1)):
    linmt1= linmt1 + 1
  for j in mt1[i]:
    colmt1 = colmt1 + 1
  dimmt1=(linmt1,colmt1)
        
  linmt2=colmt2=0
  for i in range(len(mt2)):
    linmt2= linmt2 + 1
  for j in mt2[i]:
    colmt2 = colmt2 + 1
  dimmt2=(linmt2,colmt2)

  if dimmt1 == dimmt2:
    return True
  else:
    return False


def soma_matrizes (m1,m2):
  if not compara_matriz(m1,m2):
    return False
  else:
    for i in range(len(m1)):
      for j in range(len(m1[0])):
        m1[i][j] = m1[i][j] + m2[i][j]
        
  return m1
    
