import Bhaskara
import pytest

class TestBhaskara:

  @pytest.fixture
  def b(self):
    return Bhaskara.Bhaskara()


##  @pytest.mark.parametrize("(a ,b ,c ) qtd_raizes, raiz1, raiz2", [
 #   (1, 0, 0, 1, 0),
 #   (1, -5, 6, 2, 3, 2),
   # (10, 10, 10, 0),
  ##  (10, 20, 10,1, -1)
 #   ])

  def testa_Bhaskara(a, b, c, qtd_raizes, raiz1, raiz2):
    assert b.calcura_raizes(a,b,c) == (qtd_raizes, raiz1, raiz2)
