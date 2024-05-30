#usuario add a nota
#user remove a nota
#ver as notas
#calcula as medias
#exibe maior e menor nota

#funcao para exibir o menu e input do usuario
def exibir_menu():
    print("\nGerenciador de Notas")
    print("1. Adicionar notas")
    print("2. Remover nota")
    print("3. ver Todas as Notas")
    print("4. Calcular Media das Notas")
    print("5. Exibir Maior e Menor Nota")
    print("6. Sair")
    escolha = input("Escolha uma opcao: ")
    return escolha
  
#adicionar nota
def adicionar_nota(notas):
    try:
        nota = float(input("digite a nota para adicionar: "))
        notas.append(nota)
        print("nota adicionada com sucesso.")
    except ValueError:
        print("erro: por favor, insira um valor numerico")

#remover notas
def remover_nota(notas):
    try:
        nota = float(input("digite a nota para remover: "))
        if nota in notas:
            notas.remove(nota)
            print("nota removida com sucesso")
        else:
            print("erro: nota nao encontrada")
    except ValueError:
        print("erro: por favor, insira um valor numerico")
        
#ver as notas
def ver_notas(notas):
    if notas:
        print("Notas: ", notas)
    else:
        print("nao ha notas para exibir")

#calcular as medias
def calcular_media(notas):
    if notas:
        media = sum(notas) / len(notas)
        print(f"media das notas: {media:.2f}")
    else:
        print("nao ha notas para calcular a media")
        
#calcular maior e menor nota
def exibir_maior_menor(notas):
    if notas:
        maior_nota = max(notas)
        menor_nota = min(notas)
        print(f"maior nota: {maior_nota}")
        print(f"menor nota: {menor_nota}")
    else:
        print("nao ha notas para exibir")
        
#funcao principal
def main():
    notas = []
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            adicionar_nota(notas)
        elif escolha == '2':
            remover_nota(notas)
        elif escolha == '3':
            ver_notas(notas)
        elif escolha == '4':
            calcular_media(notas)
        elif escolha == '5':
            exibir_maior_menor(notas)
        elif escolha == '6':
            print("saindo do programa...")
            break
        else:
            print("escolha invalida. Por favor, tente novamente.")        
            
if __name__ == "__main__":
    main()