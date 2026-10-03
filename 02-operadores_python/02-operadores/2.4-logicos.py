# 1 - Operador AND (E) - Retorna TRUE se todos forem verdadeiros.
tem_sol = True
tem_dinheiro = True
vai_praia = tem_sol and tem_dinheiro

print("Vai a praia (AND): ", vai_praia)

# 2 - Operador OR (OU) - Retorna TRUA se pelo menos uma condição for verdadeira.
tem_carro = False
tem_bicicleta = True
pode_viajar = tem_carro or tem_bicicleta

print("Pode viagar (OR): ", pode_viajar)

# 3 - Operador NOT (INVERSÃO) - Inverter o valor lógico.
chovendo = False
fazer_caminhada = not chovendo
print("Fazer caminhada (NOT): ", fazer_caminhada)