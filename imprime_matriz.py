def imprime_matriz(matriz):
  for i in range(len(matriz)):
    n=len(matriz[i])
    for j in matriz[i]:
      if n > 1:
        print (j , end=" ")
      else:
        print (j , end="")
      n=n-1
    print(end="\n")
