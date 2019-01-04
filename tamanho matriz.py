def dimensoes(matriz):
  col=lin=0
  for i in range(len(matriz)):
    lin= lin + 1
  for j in matriz[i]:
    col = col + 1
  print (str(lin)+"X"+str(col))
