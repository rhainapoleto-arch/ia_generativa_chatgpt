# Função completa que verifica se o número é par
def e_par(numero):
    if numero % 2 == 0:
        return True
    else: 
        False

# Usando o retorno da função em uma estrutura if e else
if e_par(12):
    print("O número é par!")
else:
    print("O número é impar!")