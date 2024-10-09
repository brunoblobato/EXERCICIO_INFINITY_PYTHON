tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluida" if tarefa['concluida'] else "Não concluida"
        print(f"{i}. {tarefa['nome']} - {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")

def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        print(f"Tarefa '{tarefas[indice]['nome']}' marcada como concluída!")
    else:
        print("Índice inválido.")

def exibir_por_prioridade(prioridade):
    filtradas = [t for t in tarefas if t['prioridade'] == prioridade]
    if not filtradas:
        print(f"Nenhuma tarefa encontrada com prioridade {prioridade}.")
    for tarefa in filtradas:
        print(f"{tarefa['nome']} - {tarefa['descricao']}")

def exibir_por_categoria(categoria):
    filtradas = [t for t in tarefas if t['categoria'] == categoria]
    if not filtradas:
        print(f"Nenhuma tarefa encontrada na categoria {categoria}.")
    for tarefa in filtradas:
        print(f"{tarefa['nome']} - {tarefa['descricao']}")

def menu():
    while True:
        print("\nGerenciador de Tarefas Diárias")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa: ")
            categoria = input("Categoria da tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            indice = int(input("Índice da tarefa a ser marcada como concluída: ")) - 1
            marcar_concluida(indice)
        elif opcao == '4':
            prioridade = input("Informe a prioridade: ")
            exibir_por_prioridade(prioridade)
        elif opcao == '5':
            categoria = input("Informe a categoria: ")
            exibir_por_categoria(categoria)
        elif opcao == '0':
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

