tentativa = 3

while tentativa !=0:
    senha = input("Digite sua senha: ")
    if senha == "123456":
        print("Bem-vindo, acesso liberado!")
        break
    else:
        print("70 de novo...")
    tentativa -= 1