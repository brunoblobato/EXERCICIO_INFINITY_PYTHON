class BombaCombustível:
    def __init__(self, tipo_combustivel, valor_litro, capacidade):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = capacidade
        self.capacidade_total = capacidade

    def abastecer_por_litro(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente na bomba de {self.tipo_combustivel}!")
            return 0, 0
        valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"\nVeículo abastecido com {litros:.2f} litros de {self.tipo_combustivel}.")
        print(f"Valor a pagar: R${valor:.2f}")
        print(f"Quantidade restante na bomba de {self.tipo_combustivel}: {self.quantidade_combustivel:.2f} litros.")
        return litros, valor


bomba_gasolina = BombaCombustível("Gasolina", 5.49, 10000)  # 10 mil litros
bomba_etanol = BombaCombustível("Etanol", 3.89, 8000)        # 8 mil litros

clientes_atendidos = []
litros_gasolina = 0
litros_etanol = 0
lucro_gasolina = 0
lucro_etanol = 0

while True:
    print("\n--- Posto de Combustível ---")
    print("1. Abastecer veículo")
    print("2. Exibir relatório do posto")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\n--- Escolha o tipo de combustível ---")
        print("1. Gasolina")
        print("2. Etanol")
        tipo_escolha = input("Escolha uma opção: ")

        if tipo_escolha == "1":
            bomba = bomba_gasolina
        elif tipo_escolha == "2":
            bomba = bomba_etanol
        else:
            print("Opção inválida!")
            continue

        try:
            litros = float(input(f"Quantos litros de {bomba.tipo_combustivel} deseja abastecer? "))
            if litros <= 0:
                print("A quantidade de litros deve ser maior que zero.")
                continue
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        litros_abastecidos, valor_pago = bomba.abastecer_por_litro(litros)
        if litros_abastecidos > 0:
            clientes_atendidos.append({"tipo": bomba.tipo_combustivel, "litros": litros_abastecidos, "valor": valor_pago})
            if bomba.tipo_combustivel == "Gasolina":
                litros_gasolina += litros_abastecidos
                lucro_gasolina += valor_pago
            elif bomba.tipo_combustivel == "Etanol":
                litros_etanol += litros_abastecidos
                lucro_etanol += valor_pago

    elif escolha == "2":
        print("\n--- Relatório do Posto ---")
        print(f"Clientes atendidos: {len(clientes_atendidos)}")
        print(f"Litros vendidos no total: {litros_gasolina + litros_etanol:.2f} litros")
        print(f" - Gasolina: {litros_gasolina:.2f} litros")
        print(f" - Etanol: {litros_etanol:.2f} litros")
        print(f"Lucro total: R${lucro_gasolina + lucro_etanol:.2f}")
        print(f" - Lucro com Gasolina: R${lucro_gasolina:.2f}")
        print(f" - Lucro com Etanol: R${lucro_etanol:.2f}")
        print(f"Combustível restante:")
        print(f"- Gasolina: {bomba_gasolina.quantidade_combustivel:.2f} litros")
        print(f"- Etanol: {bomba_etanol.quantidade_combustivel:.2f} litros")

    elif escolha == "3":
        print("\nEncerrando o programa. Obrigado!")
        break

    else:
        print("Opção inválida! Tente novamente.")
