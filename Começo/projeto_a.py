print("Cadastro para doadores de sangue")
#nome
nome = input("Insira o seu nome:")
#quilos
quilos = float(input("Insira o seu peso:"))
#altura
altura = float(input("Insira a sua altura:"))
#ano de nascimento
nascimento = int(input("Insira seu ano de nascimento: "))
idade = 2026 - nascimento
tem_peso_minimo = quilos > 50
tem_idade_minima = idade > 16
texto_saida = f"\tNOME: {nome.upper()} \n\tPESO: {quilos:.2f} \n\tALTURA: {altura:,} \n\tIDADE: {idade} \n\tTEM PESO MINIMO PARA DOAR SANGUE: {tem_peso_minimo} \n\tTEM IDADE MINIMA PARA DOAR SANGUE: {tem_idade_minima}"
print(texto_saida)
