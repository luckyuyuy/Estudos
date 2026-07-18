print("Saldão da alegria!")
total_compra = float(input("Por favor, informe o valor total da compra do cliente "))
forma_pagamento = int(input("Selicione a forma de pagamento: 1 - Boleto ou 2 - Cartão "))
if forma_pagamento == 1:
    total_compra_desconto = total_compra * 0.95
    print(f"O total da compra foi de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto. O cliente deverá pagar R${total_compra_desconto:.2f} ")
#caso a primeira condição nao seja atenfida, essa sera ativada
else:
    parcelas = int(input("Informe a quantidade de parcelas desejadas (entre 1 e 12)"))
    #dar um jeito de parar caso usuario escolha percela maior que 12
    if parcelas > 12:
        print("quantida de parcelas nao aceitas")
    valor_parcelas = total_compra / parcelas
    print(f"O total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcelas:.2f}.")