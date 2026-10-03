# Variáveis
nome = "Maria"
sobrenome = "da Silva"
nome_completo = nome + " " + sobrenome

print("Nome completo: ", nome_completo)

# Concatenação de mensagem.
idade = 32
# Alteramos o INT para STRING para poder emitir o valor inteiro usando "str(idade)"".
mensagem = "Mensagem: Olá, meu nome é " + nome_completo + " e eu tenho " + str(idade) + " anos."
print(mensagem)

# Números inseridos pelo usuário (forçamos a conversão para FLOAT)
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
nota_3 = float(input("Digite a nota 3: "))
media = (nota_1 + nota_2 + nota_3)/2
print("A média das notas é: ", media)

# Limitar o número de casas decimais.
print(f"A média das notas é: {media:.2f}")
print(f"A média das notas é: {round(media,2)}")