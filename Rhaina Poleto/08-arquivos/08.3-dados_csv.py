import csv


dados_tabela= [

["Nome", "Cargo", "idade"],
["Rhaina”, “Analista”, “18”"],
["Nathan”, “Tech Lead”, “20”"],
["Renato”, “Srum Master”, “38”"],
["Fábio”, “Product Owner”, “47”"]
]

with open("08.2-funcionarios.csv","w", encoding="utf-8", newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)