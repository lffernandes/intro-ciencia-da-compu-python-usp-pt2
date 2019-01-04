def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n - 1)

def elefantes(n, string=None):
    if n <= 1:
        return ''
    elif string == None:
        i = 1
        string = 'Um elefante incomoda muita gente '
        texto1 = 'muita gente'
        texto2 = 'muito mais'
    if i == n:
      return string
    if n > 1 and i != n:    
      while i < n:
        i += 1
        if i < n:
          if i % 2== 0:
            return elefantes(n, string = (string + str(i) + ' elefantes ' + incomodam(i) + texto2))     
          else:
            return elefantes (n, string = (string + str(i) + ' elefantes ' + incomodam(i) + texto1))
    


