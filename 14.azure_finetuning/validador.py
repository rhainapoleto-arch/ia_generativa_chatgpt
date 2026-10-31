import json

def validar_jsonl(caminho_arquivo):
    erros = 0
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        for numero_linha, linha in enumerate(f, 1):
            try:
                dados = json.loads(linha.strip())
                # Verifica se a chave 'messages' existe
                if "messages" not in dados:
                    print(f"Linha {numero_linha}: Erro - Chave 'messages' ausente.")
                    erros += 1
                    continue
                
                # Verifica se contém os papéis corretamente
                for msg in dados["messages"]:
                    if "role" not in msg or "content" not in msg:
                        print(f"Linha {numero_linha}: Erro - Mensagem mal formatada (falta 'role' ou 'content').")
                        erros += 1
            except json.JSONDecodeError:
                print(f"Linha {numero_linha}: Erro crítico - JSON inválido.")
                erros += 1
                
    if erros == 0:
        print("Sucesso! O arquivo JSONL está perfeitamente formatado para o Fine-Tuning.")
    else:
        print(f"Validação concluída com {erros} erro(s). Corrija-os antes de enviar ao Azure.")

# Teste o arquivo:
validar_jsonl("caminho_do_seu_arquivo.jsonl")