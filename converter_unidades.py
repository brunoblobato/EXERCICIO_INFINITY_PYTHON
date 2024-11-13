import tkinter as tk
from tkinter import messagebox

# Funções de conversão
def cm_para_metros():
    try:
        valor = float(entry_value.get())
        resultado = valor / 100
        label_resultado.config(text=f"Resultado: {resultado} metros")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def metros_para_cm():
    try:
        valor = float(entry_value.get())
        resultado = valor * 100
        label_resultado.config(text=f"Resultado: {resultado} cm")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def litros_para_gal():
    try:
        valor = float(entry_value.get())
        resultado = valor * 0.264172  # 1 litro = 0.264172 galão
        label_resultado.config(text=f"Resultado: {resultado} galões")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def kg_para_lbs():
    try:
        valor = float(entry_value.get())
        resultado = valor * 2.20462  # 1 kg = 2.20462 lbs
        label_resultado.config(text=f"Resultado: {resultado} lbs")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def metros_para_km():
    try:
        valor = float(entry_value.get())
        resultado = valor / 1000
        label_resultado.config(text=f"Resultado: {resultado} km")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def fahrenheit_para_celsius():
    try:
        valor = float(entry_value.get())
        resultado = (valor - 32) * 5/9
        label_resultado.config(text=f"Resultado: {resultado}°C")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Função para exibir a interface de conversão
def exibir_interface(tipo_conversao):
    # Configurações do título principal da tela
    label_titulo.config(text="Escolha o tipo de conversão no menu Conversões")

    # Reset do campo de entrada e resultado
    entry_value.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

    # Configurações específicas para cada tipo de conversão
    if tipo_conversao == "Centímetros para Metros":
        botao_convertir.config(command=cm_para_metros)
        label_input.config(text="Insira o valor em Centímetros:")
        label_explicacao.config(text="Convertendo de Centímetros para Metros")
    elif tipo_conversao == "Metros para Centímetros":
        botao_convertir.config(command=metros_para_cm)
        label_input.config(text="Insira o valor em Metros:")
        label_explicacao.config(text="Convertendo de Metros para Centímetros")
    elif tipo_conversao == "Litros para Galões":
        botao_convertir.config(command=litros_para_gal)
        label_input.config(text="Insira o valor em Litros:")
        label_explicacao.config(text="Convertendo de Litros para Galões")
    elif tipo_conversao == "Kg para Libras":
        botao_convertir.config(command=kg_para_lbs)
        label_input.config(text="Insira o valor em Kilogramas:")
        label_explicacao.config(text="Convertendo de Kilogramas para Libras")
    elif tipo_conversao == "Metros para Quilômetros":
        botao_convertir.config(command=metros_para_km)
        label_input.config(text="Insira o valor em Metros:")
        label_explicacao.config(text="Convertendo de Metros para Quilômetros")
    elif tipo_conversao == "Fahrenheit para Celsius":
        botao_convertir.config(command=fahrenheit_para_celsius)
        label_input.config(text="Insira o valor em Fahrenheit:")
        label_explicacao.config(text="Convertendo de Fahrenheit para Celsius")

# Função para mostrar a janela de menu de opções
def menu_conversao():
    janela_menu = tk.Toplevel()
    janela_menu.title("Escolha a Conversão")
    janela_menu.configure(bg="#2b2b2b")
    janela_menu.geometry("250x350")

    # Botões de conversões
    opcoes = [
        ("Centímetros para Metros", cm_para_metros),
        ("Metros para Centímetros", metros_para_cm),
        ("Litros para Galões", litros_para_gal),
        ("Kg para Libras", kg_para_lbs),
        ("Metros para Quilômetros", metros_para_km),
        ("Fahrenheit para Celsius", fahrenheit_para_celsius)
    ]
    
    for texto, funcao in opcoes:
        botao = tk.Button(
            janela_menu, text=texto,
            command=lambda f=funcao, t=texto: [exibir_interface(t)],
            bg="#4F4F4F", fg="white"
        )
        botao.pack(pady=10)

# Criando a janela principal
root = tk.Tk()
root.title("Conversor de Unidades")
root.configure(bg="#2b2b2b")
root.geometry("600x400")

# Menu principal
menu_bar = tk.Menu(root, bg="#3b3b3b", fg="white")
root.config(menu=menu_bar)
menu_opcoes = tk.Menu(menu_bar, tearoff=0, bg="#3b3b3b", fg="white")
menu_bar.add_cascade(label="Conversões", menu=menu_opcoes)
menu_opcoes.add_command(label="Escolher Conversão", command=menu_conversao)

# Título principal
label_titulo = tk.Label(root, text="Escolha o tipo de conversão no menu Conversões", font=("Arial", 16, "bold"), fg="white", bg="#2b2b2b")
label_titulo.pack(pady=10)

# Labels e botões na nova ordem
label_explicacao = tk.Label(root, text="Explicação da conversão", font=("Arial", 12), fg="#D3D3D3", bg="#2b2b2b")
label_explicacao.pack(pady=10)

label_input = tk.Label(root, text="Insira o valor a ser convertido:", font=("Arial", 12), fg="#D3D3D3", bg="#2b2b2b")
label_input.pack(pady=10)

entry_value = tk.Entry(root, font=("Arial", 12), justify="center", bg="#4F4F4F", fg="white")
entry_value.pack(pady=10)

botao_convertir = tk.Button(root, text="Converter", font=("Arial", 12), command=None, bg="#5A5A5A", fg="white")
botao_convertir.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12), fg="#D3D3D3", bg="#2b2b2b")
label_resultado.pack(pady=20)

# Inicializando com a conversão de centímetros para metros
exibir_interface("Centímetros para Metros")

# Loop principal da aplicação
root.mainloop()
