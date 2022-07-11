from Carro import Carro
from Drone import Drone
from Fila import Fila

# ---------------------- TESTES COM AS CLASSES ------------------------

# getVeiculo = Veiculo()
# getCarro = Carro("Fiat", "SUV")
# getDrone = Drone("DJI Spark", "E88 Pro")

# getVeiculo.imprimirInformacoes()
# getCarro.getInformacoes()
# getDrone.getInformacoes()


# ---------------------- DEFINIÇÃO DAS FUNÇÕES ------------------------

carroFila = Fila()
droneFila = Fila()

def adicionarCarro():

    carroMarca = input("\nDigite a Marca do Carro: ")
    carroModelo = input("Digite o Modelo do Carro: ")
    carroPortas = input("Digite a Quantidade de Portas: ")
    Carro(carroMarca, carroModelo, carroPortas)

    print ("\n---- Carros adicionados ----")
    carroFila.adicionar("\n"
                        "Marca: "+carroMarca+"\n"
                        "Modelo: "+carroModelo+"\n"
                        "Quantidade de Portas: "+carroPortas+"\n")
    carroFila.imprimir()


def adicionarDrone():

    droneMarca = input("\nDigite a Marca do Drone: ")
    droneModelo = input("Digite o Modelo do Drone: ")
    droneQntdHelices = input("Digite a Quantidade de Hélices: ")
    Drone(droneMarca, droneModelo, droneQntdHelices)
            
    print ("\n---- Drones adicionados ----")
    droneFila.adicionar("\n"
                        "Marca: "+droneMarca+"\n"
                        "Modelo: "+droneModelo+"\n"
                        "Quantidade de Hélices: "+droneQntdHelices+"\n")
    droneFila.imprimir()


def removerCarro():
    print("\nRemovendo o primeiro carro da Fila...")
    carroFila.remover()


def removerDrone():
    print("\nRemovendo o primeiro drone da Fila...")
    droneFila.remover()


def imprimirCarros():
    print("\n------ Fila de Carros cadastrados ------")
    carroFila.imprimir()


def imprimirDrones():
    print("\n------ Fila de Drones cadastrados ------")
    droneFila.imprimir()


def retornar():
    retornar = input("Retornar ao MENU? [s/n]: ")
    if retornar == "s":
        menu()
    else: 
        print("\nPrograma Finalizado.")


# ---------------------- MENU PRINCIPAL -------------------------------


def menu():
    while True:
        print('''
            MENU:
            Qual operação deseja realizar:

            [1] <-> Adicionar Carro           [5] <-> Exibir Fila de Carros
            [2] <-> Adicionar Drone           [6] <-> Exibir Fila de Drones
            [3] <-> Remover Carro     
            [4] <-> Remover Drone             [7] <-> Sair
            
        ''')

        escolha = str(input('Escolha uma opção: '))

        if escolha == "1":
            adicionarCarro()
            retornar()
            break

        elif escolha == "2":
            adicionarDrone()
            retornar()
            break

        elif escolha == "3":
            removerCarro()
            retornar()
            break

        elif escolha == "4":
            removerDrone()
            retornar()
            break

        elif escolha == "5":
            imprimirCarros()
            retornar()
            break

        elif escolha == "6":
            imprimirDrones()
            retornar()
            break

        else:
            print("Programa Finalizado.")
            break

menu()