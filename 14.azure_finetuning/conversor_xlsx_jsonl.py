import json # Usada para manipulação de arquivos JSON
import pandas as pd # Usada para manipulação de planilhas Excel

# 1. Carrega a planilha XLSX da raiz do projeto, df = dataframe
df = pd.read_excel("recursos/infraestrutura.xlsx")

# 2. Abre o arquivo JSONL de saída
arquivo_saida = "recursos/infraestrutura.jsonl"

# Com função ope em modo escrita, com codificação UTF-8(Caracteres especiais)
with open(arquivo_saida, "w", encoding="utf-8") as arquivo_jsonl:
  for index, row in df.iterrows(): # index(número linha) row(conteúdo linha) - iterate (iterar) com rows (linhas).
    # Garante que os valores sejam strings, mesmo que estejam vazios ou nulos
    system_texto = str(row["system"])
    pergunta_texto = str(row["user"])
    resposta_texto = str(row["assistant"])

    finetuning  = {
        "messages": [
            {"role": "system", "content": system_texto}, # role = system - instução IA, content = conteúdo da instrução
            {"role": "user", "content": pergunta_texto}, # role = user - pergunta do usuário, content = conteúdo da pergunta
            {"role": "assistant", "content": resposta_texto}, # role = assistant - resposta da IA, content = conteúdo da resposta
        ]
    }
    # ensure_ascii=False garante que caracteres especiais sejam mantidos no arquivo JSONL
    # json.dumps converte o dicionário em uma string JSON
    arquivo_jsonl.write(json.dumps(finetuning, ensure_ascii=False) + "\n")

print(
    f"Conversão concluída com sucesso! Arquivo '{arquivo_saida}' gerado"
    " na raiz do projeto."
)