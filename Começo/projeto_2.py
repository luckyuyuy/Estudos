opcao = 0
while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - calcular fatoria de um numero")
    print("3 - sair do programa")
    opcao = int(input("informe o numero da opcao deseja e depois tecle ENTER: "))
    if opcao == 1:
        #instrução para o caso de o usuario ter escolhido a opcao 1
        print("Voce esta amaldiçoado para todo sempre")
    elif opcao == 2:
        #instrução para o caso de o usuario ter escolhido a opcao 2
        numero = int(input("informe o numero que deseja ser calculado:"))
        fat = numero
        for valor in range(1, numero, 1):
            fat = fat * valor
        print(f"O fatorial do numero informado é: {fat}")
    elif opcao == 3:
        #instrução para o caso de o usuario ter escolhido a opcao 3
        print("Ate a proxima!")
        break
    else:
        print("Selecione uma das opcoes acima")
