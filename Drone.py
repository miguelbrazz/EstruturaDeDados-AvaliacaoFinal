    # A classe drone é composta dos atributos marca, modelo e quantidade de hélices.
    # O atributo quantidade de hélices é fortemente privado.
#   ------------------------------------------------------

from Veiculo import Veiculo

class Drone(Veiculo):

    def __init__(self, marca, modelo, qntdDeHelices = 4):
        self.marca = marca
        self.modelo = modelo
        self.__qntdDeHelices = str(qntdDeHelices)
    
    def getInformacoes(self):
        super().imprimirInformacoes()
        print("Quantidade de Hélices:", self.__qntdDeHelices)