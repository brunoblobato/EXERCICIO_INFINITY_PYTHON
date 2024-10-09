alunos = {}

def adicionar_aluno():
    numero_matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    
    if numero_matricula in alunos:
        print("Esse número de matrícula já está cadastrado.")
    else:
        alunos[numero_matricula] = nome
        print(f"Aluno {nome} adicionado com sucesso!")

def remover_aluno():
    numero_matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
    
    if numero_matricula in alunos:
        del alunos[numero_matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Número de matrícula não encontrado.")

def atualizar_aluno():
    numero_matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
    
    if numero_matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[numero_matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Número de matrícula não encontrado.")

def ver_alunos():
    if alunos:
        print("Lista de alunos:")
        for numero_matricula, nome in alunos.items():
            print(f"Número de Matrícula: {numero_matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")

def menu():
    while True:
        print("\n--- Gerenciador de Alunos ---")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            remover_aluno()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            ver_alunos()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, por favor, escolha novamente.")

if __name__ == "__main__":
    menu()
