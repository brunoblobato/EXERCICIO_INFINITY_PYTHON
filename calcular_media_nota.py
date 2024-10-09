def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado, sua média precisa ser maior ou igual a 7"

def calculadora():
    notas = []
    
    while True:
        nota = input("Digite uma nota (ou 'sair' para finalizar): ")
        
        if nota.lower() == 'sair':
            break
        
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, insira um número válido.")
    
    if notas:
        media = calcular_media(notas)
        print(f"Sua média é: {media:.2f}")
        situacao = verificar_situacao(media)
        print(situacao)
    else:
        print("Nenhuma nota foi digitada.")

if __name__ == "__main__":
    calculadora()
