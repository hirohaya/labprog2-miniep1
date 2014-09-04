from geometria.poligono import Poligono, NaoPoligono


class NaoPentagono(NaoPoligono):
    pass


class Pentagono(Poligono):
    "Classe base de um pentágono"

    def __init__(self, *lados):
        if len(lados) != 5:
            raise NaoTriangulo

        super().__init__(*lados)

class Regular(Pentagono):
<<<<<<< HEAD
    """Pentagono regular: cinco lados iguais e 540 graus de soma dos angulos internos"""
    def __init__(self, tamanho):
        super().__init__(5)
        self.tamanho = tamanho

    def perimetro(self):
        return self.lados * self.tamanho
=======
    """Implementação de um pentágono regular"""

    def __init__(self, arg):
        super(Regular, self).__init__(5) # outra forma equivalente a super()
        self.aresta = aresta

    def perimetro(self):
        per = self.aresta *self.lados

        return per
>>>>>>> origin/perimetro_pent_reg_impl2
