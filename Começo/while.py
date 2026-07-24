variavel = 0
#instrucoes a serem repitidas enquanto a condição continuar sendo verdadeira
while variavel < 10:
    print(f"Exibindo a mensagem mais uma vez... Nossa variavel vale {variavel}")
    variavel = variavel + 1

resposta = ""
while resposta.upper() != "PYTHON":
    resposta = input("digite a senha secreta: ")
print("Voce acertou! parebens ")