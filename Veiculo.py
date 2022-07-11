
class Veiculo():

    def __init__(self, marca, modelo):
        self.modelo = modelo
        self.marca = marca

    def imprimirInformacoes(self):
        dados = print("\nMarca:", self.marca, "\nModelo:", self.modelo)
        return dados