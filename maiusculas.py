def maiusculas(frase):
  m=''
  for i in range(len(frase)):
    if ord(frase[i])>= 64 and ord(frase[i])<= 96 and frase[i] != ' ':
      m +=(frase[i])
  return m
