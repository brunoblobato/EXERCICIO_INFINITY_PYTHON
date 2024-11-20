class Livro:
    def __init__(self, titulo, autor, livro_id):
        self.titulo = titulo
        self.autor = autor
        self.livro_id = livro_id
        self.status = "disponível"

    def __str__(self):
        return f"ID: {self.livro_id}, Título: {self.titulo}, Autor: {self.autor}, Status: {self.status}"


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

    def __str__(self):
        return f"Membro: {self.nome}, Número: {self.numero_membro}"


class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.membros = []

    def adicionar_livro(self, livro):
        for livro_existente in self.catalogo_livros:
            if livro_existente.livro_id == livro.livro_id:
                print(f"Erro: O ID {livro.livro_id} já está cadastrado. Tente novamente com outro ID.")
                return
        self.catalogo_livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao catálogo.")

    def adicionar_membro(self, membro):
        for membro_existente in self.membros:
            if membro_existente.numero_membro == membro.numero_membro:
                print(f"Erro: O número de membro {membro.numero_membro} já está cadastrado. Tente novamente com outro número.")
                return
        self.membros.append(membro)
        print(f"Membro {membro.nome} adicionado à biblioteca.")

    def emprestar_livro(self, membro, livro_id):
        livro = self.pesquisar_livro_por_id(livro_id)
        if livro and livro.status == "disponível":
            livro.status = "emprestado"
            membro.historico_emprestimos.append(livro)
            print(f"Livro '{livro.titulo}' emprestado para {membro.nome}.")
        elif livro:
            print(f"Desculpe, o livro '{livro.titulo}' já está emprestado.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, membro, livro_id):
        livro = self.pesquisar_livro_por_id(livro_id)
        if livro in membro.historico_emprestimos:
            livro.status = "disponível"
            membro.historico_emprestimos.remove(livro)
            print(f"Livro '{livro.titulo}' devolvido por {membro.nome}.")
        else:
            print(f"{membro.nome} não possui este livro.")

    def pesquisar_livro_por_titulo(self, titulo):
        livros_encontrados = [livro for livro in self.catalogo_livros if titulo.lower() in livro.titulo.lower()]
        return livros_encontrados

    def pesquisar_livro_por_autor(self, autor):
        livros_encontrados = [livro for livro in self.catalogo_livros if autor.lower() in livro.autor.lower()]
        return livros_encontrados

    def pesquisar_livro_por_id(self, livro_id):
        for livro in self.catalogo_livros:
            if livro.livro_id == livro_id:
                return livro
        return None

    def exibir_catalogo(self):
        if not self.catalogo_livros:
            print("O catálogo está vazio.")
        else:
            for livro in self.catalogo_livros:
                print(livro)

    def exibir_membros(self):
        if not self.membros:
            print("Nenhum membro registrado.")
        else:
            for membro in self.membros:
                print(membro)


def menu():
    biblioteca = Biblioteca()

    livro1 = Livro("Dom Casmurro", "Machado de Assis", "1")
    livro2 = Livro("O Primo Basílio", "José de Alencar", "2")
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Adicionar membro")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Pesquisar livro por título")
        print("6. Pesquisar livro por autor")
        print("7. Exibir catálogo de livros")
        print("8. Exibir membros")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro_id = input("Digite o ID do livro: ")
            livro = Livro(titulo, autor, livro_id)
            biblioteca.adicionar_livro(livro)
        elif opcao == '2':
            nome = input("Digite o nome do membro: ")
            numero_membro = input("Digite o número do membro: ")
            membro = Membro(nome, numero_membro)
            biblioteca.adicionar_membro(membro)
        elif opcao == '3':
            numero_membro = input("Digite o número do membro: ")
            livro_id = input("Digite o ID do livro a ser emprestado: ")
            membro = next((m for m in biblioteca.membros if m.numero_membro == numero_membro), None)
            if membro:
                biblioteca.emprestar_livro(membro, livro_id)
            else:
                print("Membro não encontrado.")
        elif opcao == '4':
            numero_membro = input("Digite o número do membro: ")
            livro_id = input("Digite o ID do livro a ser devolvido: ")
            membro = next((m for m in biblioteca.membros if m.numero_membro == numero_membro), None)
            if membro:
                biblioteca.devolver_livro(membro, livro_id)
            else:
                print("Membro não encontrado.")
        elif opcao == '5':
            titulo = input("Digite o título do livro para pesquisa: ")
            livros = biblioteca.pesquisar_livro_por_titulo(titulo)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro encontrado com esse título.")
        elif opcao == '6':
            autor = input("Digite o autor do livro para pesquisa: ")
            livros = biblioteca.pesquisar_livro_por_autor(autor)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro encontrado com esse autor.")
        elif opcao == '7':
            biblioteca.exibir_catalogo()
        elif opcao == '8':
            biblioteca.exibir_membros()
        elif opcao == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
