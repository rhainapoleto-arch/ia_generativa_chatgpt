# Lista de arquivos encontrados no diretório.
arquivos_enviados = ["manual.pdf", "foto.png", "contrato.PDF","relatorio.pdf","anotacoes.txt"]

# Lista de arquivos PDF (vazia).
pdfs_validos = []

for arquivo in arquivos_enviados:
    if arquivo.lower().endswith(".pdf"):
        pdfs_validos.append(arquivo)

print("Arquivos enviados foram...", arquivos_enviados)
print("Arquivos de PDFs válidos foram...", pdfs_validos)