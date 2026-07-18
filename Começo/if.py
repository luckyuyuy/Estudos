print("Quilão do lucas")
preco_quilo = float(input("Informe o valor cobrado por quilo!: "))
peso_prato = float(input("informe o peso do prato do cliente (em kg): "))
preco_prato = preco_quilo * peso_prato
print(f"O valor do prato é R${preco_prato:.2f}")
#o desvio abaixo testa se o peso do prato ultrapassa 1kg e xibe a ensagem apenas
if peso_prato >= 1:
    print("O preco exedeu 1kg. O cliente pode pagar R$80,00 e consumir à vontade!")