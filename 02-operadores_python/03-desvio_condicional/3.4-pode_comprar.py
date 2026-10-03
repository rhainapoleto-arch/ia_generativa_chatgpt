# Exemplo de Encadeamento ou Aninhamento
tem_cartao = True
saldo = 200.0

if tem_cartao:
    if saldo >= 100:
        print("Compra aprovada, saldo suficiente...")
    else:
        print("Compra negada, saldo insuficiente...")

else:
    print("Erro, cartão não inserido!")