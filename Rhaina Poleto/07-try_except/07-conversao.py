entrada_usuario = "abc"

try:
    numero_convertido = int(entrada_usuario)
    print("Conversão realizada com sucesso: ", numero_convertido)

except: 
    print("Erro: Você precisa digitar somente números válidos!")