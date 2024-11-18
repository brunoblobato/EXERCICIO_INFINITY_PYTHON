class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def entrar(self, pessoas):
        if self.atualCapacidade + pessoas <= self.totalCapacidade:
            self.atualCapacidade += pessoas
            print(f"{pessoas} pessoa(s) entrou(ram) no elevador.")
            restante = self.totalCapacidade - self.atualCapacidade
            print(f"Ainda cabem {restante} pessoa(s) no elevador. Capacidade máxima {self.totalCapacidade} pessoas.")
        else:
            print("O ELEVADOR ESTÁ CHEIO! Não é possível adicionar tantas pessoas.")

    def sair(self):
        if self.atualCapacidade > 0:
            print(f"Saindo {self.atualCapacidade} pessoa(s).")
            self.atualCapacidade = 0
        else:
            print("NÃO TEM NINGUÉM NO ELEVADOR!")

    def subir(self, andarDestino):
        if andarDestino > self.atualAndar and andarDestino <= self.totalAndar - 1:
            for andar in range(self.atualAndar + 1, andarDestino + 1):
                print(f"Subindo para o andar {andar}...")
            self.atualAndar = andarDestino
            print(f"Chegamos ao andar {andarDestino}. As portas se abriram!")
        elif andarDestino == self.atualAndar:
            print("Você já está neste andar.")
        else:
            print("VOCÊ ESTÁ NO ÚLTIMO ANDAR OU ANDAR INVÁLIDO!")

    def descer(self, andarDestino):
        if andarDestino < self.atualAndar and andarDestino >= 0:
            for andar in range(self.atualAndar - 1, andarDestino - 1, -1):
                print(f"Descendo para o andar {andar}...")
            self.atualAndar = andarDestino
            print(f"Chegamos ao andar {andarDestino}. As portas se abriram!")
        elif andarDestino == self.atualAndar:
            print("Você já está neste andar.")
        else:
            print("VOCÊ ESTÁ NO TÉRREO OU ANDAR INVÁLIDO!")


def menu_elevador():
    elevador = Elevador(totalCapacidade=5, totalAndar=11)

    while True:
        print("\n--- Menu Inicial ---")
        print("1. Entrar no elevador")
        print("2. Sair do programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pessoas = int(input("Quantas pessoas estão entrando? "))
            elevador.entrar(pessoas)

            while elevador.atualCapacidade > 0:
                andarDestino = int(input("Para qual andar deseja ir (0-10)? "))
                if andarDestino > elevador.atualAndar:
                    elevador.subir(andarDestino)
                elif andarDestino < elevador.atualAndar:
                    elevador.descer(andarDestino)
                else:
                    print("Você já está neste andar. Escolha outra opção.")

                while True:
                    print("\n--- Opções no Elevador ---")
                    print("1. Sair do elevador")
                    print("2. Subir")
                    print("3. Descer")
                    escolha = input("Escolha uma opção: ")

                    if escolha == "1":
                        elevador.sair()
                        print("Elevador livre para próxima viagem!")
                        break
                    elif escolha == "2":
                        andarDestino = int(input("Para qual andar deseja ir (0-10)? "))
                        if andarDestino > elevador.atualAndar:
                            elevador.subir(andarDestino)
                        else:
                            print("Você deve escolher um andar acima do atual.")
                    elif escolha == "3":
                        andarDestino = int(input("Para qual andar deseja ir (0-10)? "))
                        if andarDestino < elevador.atualAndar:
                            elevador.descer(andarDestino)
                        else:
                            print("Você deve escolher um andar abaixo do atual.")
                    else:
                        print("Opção inválida.")
                break
        elif opcao == "2":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu_elevador()
