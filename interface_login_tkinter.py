import tkinter as tk
from tkinter import messagebox

# Função para validar o login
def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    # Validações
    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter '@'.")
    elif len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 caracteres.")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        # Aqui você pode adicionar a lógica para prosseguir após o login.

# Criando a janela principal
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x300")
root.configure(bg="#2b2b2b")

# Título
label_titulo = tk.Label(root, text="Tela de Login", font=("Arial", 16, "bold"), fg="white", bg="#2b2b2b")
label_titulo.pack(pady=10)

# Campo de e-mail
label_email = tk.Label(root, text="E-mail:", font=("Arial", 12), fg="white", bg="#2b2b2b")
label_email.pack(anchor="w", padx=20)
entry_email = tk.Entry(root, font=("Arial", 12), bg="#4F4F4F", fg="white")
entry_email.pack(pady=5, padx=20, fill="x")

# Campo de senha
label_senha = tk.Label(root, text="Senha:", font=("Arial", 12), fg="white", bg="#2b2b2b")
label_senha.pack(anchor="w", padx=20)
entry_senha = tk.Entry(root, font=("Arial", 12), show="*", bg="#4F4F4F", fg="white")
entry_senha.pack(pady=5, padx=20, fill="x")

# Botão de login
botao_login = tk.Button(root, text="Login", font=("Arial", 12), command=validar_login, bg="#5A5A5A", fg="white")
botao_login.pack(pady=20)

# Iniciar a aplicação
root.mainloop()
