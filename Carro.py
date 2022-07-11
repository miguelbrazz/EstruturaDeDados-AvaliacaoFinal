    # A classe carro é composta dos atributos marca, modelo e portas.
    # O atributo portas é fracamente privado.
#   ------------------------------------------------------

from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas = 4):
        self.marca = marca
        self.modelo = modelo
        self._portas = str(portas)

    def getInformacoes(self):
        super().imprimirInformacoes()
        print("Quantidade de Portas:", self._portas)