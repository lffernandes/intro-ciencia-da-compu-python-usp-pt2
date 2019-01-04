

class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def main(self):
    return self.perimetro()

  def perimetro(self):
    p = (self.a + self.b + self.c)
    return p
  
  def tipo_lado(self):
    if self.isoceles():
      return 'isóceles'
    elif self.equilatero():
      return 'equilátero'
    elif self.escaleno():
      return 'escaleno'

  def isoceles(self):
    if self.a == self.b or self.a == self.c or self.b == self.c:
      if self.b != self.c:
        return True
      elif self.a != self.b:
        return True
      else:
        return False

  def equilatero(self):
    if self.a == self.b == self.c:
      return True
    else:
      return False

  def escaleno(self):
    if self.a != self.b != self.c:
      return True

  def retangulo(self):  
    if self.c**2 == self.a**2 + self.b**2:
      return True
    else:
      return False
    
  def semelhantes(self, t):
    list_self=sorted([self.a , self.b, self.c])
    list_t=sorted([t.a , t.b, t.c])
    if list_self == list_t :
     return True
    else:
      return False
  
