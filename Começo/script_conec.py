usuario = input("Informe o usuario que deseja acessar o sistema: ")
senha = input("Informe a senha do usuario que deseja acessar o sistema:")
if usuario.upper() == "ADMIN" and senha == "123":
    print("Acesso autorizado!")
else:
    print("Usuario ou senha incorreta. Acesso negado!")