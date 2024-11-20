import tkinter as tk
from tkinter import messagebox

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
                return "Erro: O ID do livro já está cadastrado."
        self.catalogo_livros.append(livro)
        return f"Livro '{livro.titulo}' adicionado ao catálogo."

    def adicionar_membro(self, membro):
        for membro_existente in self.membros:
            if membro_existente.numero_membro == membro.numero_membro:
                return "Erro: O número de membro já está cadastrado."
        self.membros.append(membro)
        return f"Membro {membro.nome} adicionado à biblioteca."

    def emprestar_livro(self, membro, livro_id):
        livro = self.pesquisar_livro_por_id(livro_id)
        if livro and livro.status == "disponível":
            livro.status = "emprestado"
            membro.historico_emprestimos.append(livro)
            return f"Livro '{livro.titulo}' emprestado para {membro.nome}."
        elif livro:
            return f"Desculpe, o livro '{livro.titulo}' já está emprestado."
        else:
            return "Livro não encontrado."

    def devolver_livro(self, membro, livro_id):
        livro = self.pesquisar_livro_por_id(livro_id)
        if livro in membro.historico_emprestimos:
            livro.status = "disponível"
            membro.historico_emprestimos.remove(livro)
            return f"Livro '{livro.titulo}' devolvido por {membro.nome}."
        else:
            return f"{membro.nome} não possui este livro."

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
        return "\n".join(str(livro) for livro in self.catalogo_livros)

    def exibir_membros(self):
        return "\n".join(str(membro) for membro in self.membros)


class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca - Gerenciamento")
        self.root.geometry("600x550")
        self.root.configure(bg="black")

        self.biblioteca = Biblioteca()

        livro1 = Livro("Dom Casmurro", "Machado de Assis", "1")
        livro2 = Livro("O Primo Basílio", "José de Alencar", "2")
        self.biblioteca.adicionar_livro(livro1)
        self.biblioteca.adicionar_livro(livro2)

        # Configurações da interface gráfica
        self.create_widgets()

    def create_widgets(self):
        # Título e Instruções
        self.title_label = tk.Label(self.root, text="Gerenciamento de Biblioteca", font=("Helvetica", 16), bg="black", fg="white")
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(self.root, text="Escolha uma opção abaixo para continuar.", font=("Helvetica", 12), bg="black", fg="white")
        self.instructions_label.pack(pady=5)

        # Botões
        self.add_book_button = tk.Button(self.root, text="Adicionar Livro", font=("Helvetica", 12), bg="green", fg="white", command=self.add_book, relief="solid", bd=3, width=20)
        self.add_book_button.pack(fill="x", padx=20, pady=5)

        self.add_member_button = tk.Button(self.root, text="Adicionar Membro", font=("Helvetica", 12), bg="green", fg="white", command=self.add_member, relief="solid", bd=3, width=20)
        self.add_member_button.pack(fill="x", padx=20, pady=5)

        self.borrow_book_button = tk.Button(self.root, text="Emprestar Livro", font=("Helvetica", 12), bg="green", fg="white", command=self.borrow_book, relief="solid", bd=3, width=20)
        self.borrow_book_button.pack(fill="x", padx=20, pady=5)

        self.return_book_button = tk.Button(self.root, text="Devolver Livro", font=("Helvetica", 12), bg="green", fg="white", command=self.return_book, relief="solid", bd=3, width=20)
        self.return_book_button.pack(fill="x", padx=20, pady=5)

        self.search_book_button = tk.Button(self.root, text="Pesquisar Livro", font=("Helvetica", 12), bg="green", fg="white", command=self.search_book, relief="solid", bd=3, width=20)
        self.search_book_button.pack(fill="x", padx=20, pady=5)

        self.view_catalog_button = tk.Button(self.root, text="Exibir Catálogo de Livros", font=("Helvetica", 12), bg="green", fg="white", command=self.view_catalog, relief="solid", bd=3, width=20)
        self.view_catalog_button.pack(fill="x", padx=20, pady=5)

        self.view_members_button = tk.Button(self.root, text="Exibir Membros", font=("Helvetica", 12), bg="green", fg="white", command=self.view_members, relief="solid", bd=3, width=20)
        self.view_members_button.pack(fill="x", padx=20, pady=5)

        self.result_label = tk.Label(self.root, text="O resultado da pesquisa:", font=("Helvetica", 10), bg="black", fg="white")
        self.result_label.pack(pady=5)

        self.message_box = tk.Text(self.root, height=10, width=70, wrap="word", font=("Helvetica", 10), bg="black", bd=3, fg="white")
        self.message_box.pack(pady=10)

    def clear_message_box(self):
        self.message_box.delete(1.0, tk.END)

    def show_message(self, message):
        self.clear_message_box()
        self.message_box.insert(tk.END, message)

    def add_book(self):
        self.clear_message_box()
        book_window = tk.Toplevel(self.root)
        book_window.title("Adicionar Livro")
        book_window.geometry("400x300")
        book_window.configure(bg="black")

        tk.Label(book_window, text="Título do Livro:", bg="black", fg="white").pack(pady=5)
        title_entry = tk.Entry(book_window)
        title_entry.pack(pady=5)

        tk.Label(book_window, text="Autor do Livro:", bg="black", fg="white").pack(pady=5)
        author_entry = tk.Entry(book_window)
        author_entry.pack(pady=5)

        tk.Label(book_window, text="ID do Livro:", bg="black", fg="white").pack(pady=5)
        id_entry = tk.Entry(book_window)
        id_entry.pack(pady=5)

        def submit_book():
            title = title_entry.get()
            author = author_entry.get()
            book_id = id_entry.get()
            livro = Livro(title, author, book_id)
            result = self.biblioteca.adicionar_livro(livro)
            self.show_message(result)
            book_window.destroy()

        submit_button = tk.Button(book_window, text="Cadastrar Livro", bg="green", fg="white", command=submit_book, relief="solid", bd=3)
        submit_button.pack(pady=10)

    def add_member(self):
        self.clear_message_box()
        member_window = tk.Toplevel(self.root)
        member_window.title("Adicionar Membro")
        member_window.geometry("400x300")
        member_window.configure(bg="black")

        tk.Label(member_window, text="Nome do Membro:", bg="black", fg="white").pack(pady=5)
        name_entry = tk.Entry(member_window)
        name_entry.pack(pady=5)

        tk.Label(member_window, text="Número do Membro:", bg="black", fg="white").pack(pady=5)
        number_entry = tk.Entry(member_window)
        number_entry.pack(pady=5)

        def submit_member():
            name = name_entry.get()
            number = number_entry.get()
            member = Membro(name, number)
            result = self.biblioteca.adicionar_membro(member)
            self.show_message(result)
            member_window.destroy()

        submit_button = tk.Button(member_window, text="Cadastrar Membro", bg="green", fg="white", command=submit_member, relief="solid", bd=3)
        submit_button.pack(pady=10)

    def borrow_book(self):
        self.clear_message_box()
        borrow_window = tk.Toplevel(self.root)
        borrow_window.title("Emprestar Livro")
        borrow_window.geometry("400x250")
        borrow_window.configure(bg="black")

        tk.Label(borrow_window, text="Número do Membro:", bg="black", fg="white").pack(pady=5)
        member_number_entry = tk.Entry(borrow_window)
        member_number_entry.pack(pady=5)

        tk.Label(borrow_window, text="ID do Livro:", bg="black", fg="white").pack(pady=5)
        book_id_entry = tk.Entry(borrow_window)
        book_id_entry.pack(pady=5)

        def submit_borrow():
            member_number = member_number_entry.get()
            book_id = book_id_entry.get()
            member = next((membro for membro in self.biblioteca.membros if membro.numero_membro == member_number), None)
            if member:
                result = self.biblioteca.emprestar_livro(member, book_id)
                self.show_message(result)
                borrow_window.destroy()
            else:
                self.show_message("Membro não encontrado!")

        submit_button = tk.Button(borrow_window, text="Emprestar Livro", bg="green", fg="white", command=submit_borrow, relief="solid", bd=3)
        submit_button.pack(pady=10)

    def return_book(self):
        self.clear_message_box()
        return_window = tk.Toplevel(self.root)
        return_window.title("Devolver Livro")
        return_window.geometry("400x250")
        return_window.configure(bg="black")

        tk.Label(return_window, text="Número do Membro:", bg="black", fg="white").pack(pady=5)
        member_number_entry = tk.Entry(return_window)
        member_number_entry.pack(pady=5)

        tk.Label(return_window, text="ID do Livro:", bg="black", fg="white").pack(pady=5)
        book_id_entry = tk.Entry(return_window)
        book_id_entry.pack(pady=5)

        def submit_return():
            member_number = member_number_entry.get()
            book_id = book_id_entry.get()
            member = next((membro for membro in self.biblioteca.membros if membro.numero_membro == member_number), None)
            if member:
                result = self.biblioteca.devolver_livro(member, book_id)
                self.show_message(result)
                return_window.destroy()
            else:
                self.show_message("Membro não encontrado!")

        submit_button = tk.Button(return_window, text="Devolver Livro", bg="green", fg="white", command=submit_return, relief="solid", bd=3)
        submit_button.pack(pady=10)

    def search_book(self):
        self.clear_message_box()
        search_window = tk.Toplevel(self.root)
        search_window.title("Pesquisar Livro")
        search_window.geometry("400x300")
        search_window.configure(bg="black")

        tk.Label(search_window, text="Título do Livro:", bg="black", fg="white").pack(pady=5)
        title_entry = tk.Entry(search_window)
        title_entry.pack(pady=5)

        tk.Label(search_window, text="Autor do Livro:", bg="black", fg="white").pack(pady=5)
        author_entry = tk.Entry(search_window)
        author_entry.pack(pady=5)

        def submit_search():
            title = title_entry.get()
            author = author_entry.get()
            result = self.biblioteca.pesquisar_livro_por_titulo(title) + self.biblioteca.pesquisar_livro_por_autor(author)
            if result:
                self.show_message("\n".join(str(livro) for livro in result))
            else:
                self.show_message("Livro não encontrado!")

        submit_button = tk.Button(search_window, text="Pesquisar", bg="green", fg="white", command=submit_search, relief="solid", bd=3)
        submit_button.pack(pady=10)

    def view_catalog(self):
        self.clear_message_box()
        catalog = self.biblioteca.exibir_catalogo()
        self.show_message(catalog if catalog else "Catálogo vazio!")

    def view_members(self):
        self.clear_message_box()
        members = self.biblioteca.exibir_membros()
        self.show_message(members if members else "Nenhum membro cadastrado!")

root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()
