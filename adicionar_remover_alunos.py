def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno '{nome}' adicionado com sucesso!")

def remover_aluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno com matrícula '{matricula}' removido com sucesso!")
    else:
        print("Matrícula não encontrada.")

def visualizar_alunos(alunos):
    if alunos:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno registrado.")

def menu():
    alunos = {}
    
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Visualizar alunos")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            adicionar_aluno(alunos)
        elif escolha == '2':
            remover_aluno(alunos)
        elif escolha == '3':
            visualizar_alunos(alunos)
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
