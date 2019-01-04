import pytest
import cria_lista_aleat
import ordena_lista

def merge_sort(lista):
  if len(lista) <=1:  #BASE DA RECURSAO
    return lista

  meio = len(lista) // 2

  lado_esquerdo = merge_sort(lista[:meio])
  lado_direito = merge_sort(lista[meio:])

  return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
  if not lado_esquerdo:
    return lado_direito

  if not lado_direito:
    return lado_esquerdo

  if lado_esquerdo[0] < lado_direito[0]:
    return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

  return[lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


@pytest.mark.parametrize("lista, esperado", [
   ([8,3,6,1,12,89,40,29],[1,3,6,8,12,29,40,89]),
   ([103,140,137,154,176,189,199,100],[100,103,137,140,154,176,189,199]),
   ([217, 930, 481, 650, 113, 491, 595, 755],[113, 217, 481, 491, 595, 650, 755, 930]),
   ([395, 242, 544, 569, 869, 162, 896, 966],[162, 242, 395, 544, 569, 869, 896, 966]),
   ([418, 658, 165, 187, 994, 738, 270, 282],[165, 187, 270, 282, 418, 658, 738, 994]),
   ([8, 629, 494, 457, 932, 34, 769, 144],[8, 34, 144, 457, 494, 629, 769, 932])
   
   ])

def testa_merge_sort(lista,esperado):
   assert merge_sort(lista) == esperado
