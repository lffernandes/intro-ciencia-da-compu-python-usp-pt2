import pytest

def busca_binaria(lista, elemento, min=0, max=None):
  
    if max == None:
        max = len(lista)-1
      
    if max < min:
      return False
    else:
      meio = min +(max-min)//2

    if lista[meio] > elemento:
      return busca_binaria(lista, elemento, min, meio-1)

    elif lista[meio] < elemento:
      return busca_binaria(lista, elemento, meio+1, max)

    else:
      return meio

a = [13, 34, 41, 57, 60, 90, 102]

@pytest.mark.parametrize("lista, valor, esperado", [
      (a, 13, 0),
      (a, 34, 1),
      (a, 41, 2),
      (a, 57, 3),
      (a, 60, 4),
      (a, 90, 5),
      (a, 102, 6),
      (a, -13, False),
      (a, 12, False),
      (a, 103, False)
      ])

def testa_busca_binaria(lista, valor, esperado): 
      assert busca_binaria(lista, valor) == esperado
