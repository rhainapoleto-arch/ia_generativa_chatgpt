# O mo w cria o arquivo "relatorio.txt" na pasta raiz do projeto
with open("08-relatorio.txt","a",encoding= "utf-8") as arquivos:
    arquivos.write("Primeira linha: atenção a primeira linha foi escrita\n")
    arquivos.write("\nSegunda linha: Dados processados com sucesso!")