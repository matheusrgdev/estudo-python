#Integrantes
# Matheus Ferreira Rodrigues Santos - 12511GIN020

def multiplos_intervalo():
    try:
        A = int(input("Digite o valor inicial do intervalo(A):"))
        B = int(input("Digite o valor final do intervalo(B):"))
        C = int(input("Digite o valor do número que deseja calcular os múltiplos no intervalo(C):"))

    except ValueError:
        print("Erro: Digite apenas números inteiros.")
        return

    if B <= A:
        print("Digite um valor de B que seja maior que A.")
        return
    if C < 3:
        print("Erro: O valor de C deve ser maior ou igual a 3.")
        return
        
    multiplos = []
    for i in range(A, B+1):
        if i % C == 0:
            multiplos.append(i)
    
    if multiplos:
        print(f"Múltiplos de {C} no intervalo: de {A} até {B} {multiplos}")
    else:
        print(f"O intervalo não contém múltiplos de {C}.")


def percurso():
    try:
        A = int(input("Digite um número para ser o ponto inicial(A):"))
        B = int(input("Digite um número para ser o ponto final(B):"))

        if A == B:
            print("Erro: A não pode ser igual a B.")
            return
        
        if B > A:
            for i in range(A, B + 1):
                print(i, end=" ")
        else:
            for i in range(A, B - 1, -1):
                print(i, end=" ")
        print()
    
    except ValueError:
        print("Erro: Digite apenas números inteiros.")


def fibonacci():
    try:
        N = int(input("Digite um número maior ou igual a 3: "))
        if N < 3:
            print("Erro: N deve ser maior ou igual a 3.")
            return
        
        a, b = 0, 1
        print(a, b, end=" ")
        for _ in range(2, N):
            a, b = b, a + b
            print(b, end=" ")
        print()
    
    except ValueError:
        print("Erro: Digite apenas números inteiros.")


def tabuada_personalizada():
    try:
        A = int(input("Digite o número para a tabuada(A): "))
        B = int(input("Digite o valor inicial do intervalo(B): "))
        C = int(input("Digite o valor final do intervalo(C): "))

        if A < 1:
            print("Erro: A deve ser maior ou igual a 1.")
            return
        
        if C < B:
            print("Erro: O valor final deve ser maior que o valor inicial.")
            return
        
        for i in range(B, C + 1):
            print(f"{A} x {i} = {A * i}")
    
    except ValueError:
        print("Erro: Digite apenas números inteiros.")


def compra_parcelada():
    try:
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        parcelas = int(input("Digite o número de parcelas: "))

        if preco < 10:
            print("Erro: O preço mínimo é de R$10,00.")
            return
        
        if parcelas <= 1:
            print("Erro: O mínimo para calcular os juros são 2 parcelas.")
            return
        
        i = 0.03
        total = preco * (1 + i * parcelas)

        print()
        print(f"Produto: {produto}")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor total com juros: {total}")
    
    except ValueError:
        print("Erro: Digite valores válidos.")


def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1 - Para calcular múltiplos em um intervalo")
        print("2 - Para calcular um percuso entre 2 números")
        print("3 - Para calcular a sequência de Fibonacci")
        print("4 - Para calcular a tabuada personalizada de um número")
        print("5 - Para calcular o valor total de uma compra parcelada")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            multiplos_intervalo()
        elif opcao == "2":
            percurso()
        elif opcao == "3":
            fibonacci()
        elif opcao == "4":
            tabuada_personalizada()
        elif opcao == "5":
            compra_parcelada()
        elif opcao == "0":
            print("Programa finalizado. Agradecemos a sua utilização! :)")
            break
        else:
            print(":( Opção Inválida! Você tem outra chance para tentar novamente.")

menu()