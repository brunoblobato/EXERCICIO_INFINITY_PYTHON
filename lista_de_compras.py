lista_produtos = []
totalProdutos = 0

def exibir_menu():
    print("\n--- Menu de Opções ---")
    print("1. Adicionar produto")
    print("2. Ver lista de produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Encerrar programa")
    escolha = input("Escolha uma opção: ")
    return escolha

def adicionar_produto():
    global totalProdutos
    nome = input("Nome do produto: ")
    
    while True:
        try:
            quantidade = int(input("Quantidade (apenas números inteiros): "))
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar apenas números inteiros para a quantidade.")

    while True:
        try:
            valor_unitario = float(input("Valor unitário (use ponto para decimais): "))
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de usar ponto (.) como separador decimal e insira apenas números.")

    total = quantidade * valor_unitario
    produto = {
        "nome": nome,
        "valor": valor_unitario,
        "quantidade": quantidade,
        "total": total
    }
    lista_produtos.append(produto)
    totalProdutos += total
    print(f"Produto '{nome}' adicionado com sucesso.")

def ver_lista_produtos():
    global totalProdutos
    if not lista_produtos:
        print("A lista de produtos está vazia.")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in lista_produtos:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, "
                  f"Valor Unitário: {produto['valor']:.2f}, Total: {produto['total']:.2f}")
        print(f"Valor total de todos os produtos: {totalProdutos:.2f}")

def atualizar_produto():
    global totalProdutos
    nome = input("Nome do produto a ser atualizado: ")
    for produto in lista_produtos:
        if produto['nome'] == nome:
            totalProdutos -= produto['total']

            novo_nome = input("Novo nome do produto: ") or produto['nome']
            
            while True:
                try:
                    nova_quantidade = int(input("Nova quantidade (apenas números inteiros): ") or produto['quantidade'])
                    break
                except ValueError:
                    print("Entrada inválida. Certifique-se de digitar apenas números inteiros para a quantidade.")

            while True:
                try:
                    novo_valor_unitario = float(input("Novo valor unitário (use ponto para decimais): ") or produto['valor'])
                    break
                except ValueError:
                    print("Entrada inválida. Certifique-se de usar ponto (.) como separador decimal e insira apenas números.")

            produto['nome'] = novo_nome
            produto['quantidade'] = nova_quantidade
            produto['valor'] = novo_valor_unitario
            produto['total'] = nova_quantidade * novo_valor_unitario

            totalProdutos += produto['total']
            print(f"Produto '{nome}' atualizado com sucesso.")
            return

    print(f"Produto '{nome}' não encontrado na lista.")

def remover_produto():
    global totalProdutos
    nome = input("Nome do produto a ser removido: ")
    for produto in lista_produtos:
        if produto['nome'] == nome:
            totalProdutos -= produto['total']
            lista_produtos.remove(produto)
            print(f"Produto '{nome}' removido com sucesso.")
            return

    print(f"Produto '{nome}' não encontrado na lista.")

def principal():
    while True:
        escolha = exibir_menu()
        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            ver_lista_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            remover_produto()
        elif escolha == "5":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    principal()
