class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor/Editor(a): {self.autor_ou_editora}")


class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Gênero: {self.genero}")


class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Edição: {self.edicao}")


class Biblioteca:
    def __init__(self):
        self.materials = []

    def exibir_materiais(self):
        if not self.materials:
            print("Não há materiais cadastrados.\n")
        for i, material in enumerate(self.materials, start=1):
            print(f"\nMaterial {i}:")
            material.exibir_informacoes()

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor_ou_editora = input("Digite o autor do livro: ")
        genero = input("Digite o gênero do livro: ")
        livro = Livro(titulo, autor_ou_editora, genero)
        self.materials.append(livro)
        print("\nLivro cadastrado com sucesso!")

    def cadastrar_revista(self):
        titulo = input("Digite o título da revista: ")
        autor_ou_editora = input("Digite a editora da revista: ")
        edicao = input("Digite a edição da revista: ")
        revista = Revista(titulo, autor_ou_editora, edicao)
        self.materials.append(revista)
        print("\nRevista cadastrada com sucesso!")

    def editar_material(self):
        self.exibir_materiais()
        index = int(input("\nDigite o número do material que deseja editar: ")) - 1
        if index < 0 or index >= len(self.materials):
            print("Material não encontrado.")
            return
        material = self.materials[index]

        if isinstance(material, Livro):
            print("\nEditando Livro...")
            material.titulo = input("Novo título: ")
            material.autor_ou_editora = input("Novo autor: ")
            material.genero = input("Novo gênero: ")
        elif isinstance(material, Revista):
            print("\nEditando Revista...")
            material.titulo = input("Novo título: ")
            material.autor_ou_editora = input("Nova editora: ")
            material.edicao = input("Nova edição: ")

        print("\nMaterial editado com sucesso!")

    def deletar_material(self):
        self.exibir_materiais()
        index = int(input("\nDigite o número do material que deseja excluir: ")) - 1
        if index < 0 or index >= len(self.materials):
            print("Material não encontrado.")
            return
        self.materials.pop(index)
        print("\nMaterial excluído com sucesso!")


def menu():
    biblioteca = Biblioteca()
    # Livros e revistas iniciais
    livro = Livro("Dom Casmurro", "Machado de Assis", "Romance")
    revista = Revista("Revista Veja", "Editora Abril", "Edição 1000")
    biblioteca.materials.append(livro)
    biblioteca.materials.append(revista)

    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Listar acervo")
        print("2. Cadastrar novo livro")
        print("3. Cadastrar nova revista")
        print("4. Editar material")
        print("5. Deletar material")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            biblioteca.exibir_materiais()
        elif opcao == '2':
            biblioteca.cadastrar_livro()
        elif opcao == '3':
            biblioteca.cadastrar_revista()
        elif opcao == '4':
            biblioteca.editar_material()
        elif opcao == '5':
            biblioteca.deletar_material()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
