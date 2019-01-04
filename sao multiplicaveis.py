def sao_multiplicaveis(m1,m2):
  m=False
  for i1 in range(len(m1)):
    for j1 in m1[i1]:
      print(i1,j1,)
      pass
    for i2 in range(len(m2)):
      for j2 in m2[i2]:
        print(i2,j2,)
        if j1%j2==0:
          m = True
          pass
        else:
          m = False
          pass
        pass  
  return m

      
        
