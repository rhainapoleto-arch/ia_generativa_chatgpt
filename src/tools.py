import os
import shutil
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from src.config import azure_embeddings
from langchain_core.tools import tool

PASTA_PDFS = "pdfs"
DIRETORIO_DB = "chroma_db"

def processar_pdf():
    """Limpa e recria o banco vetorial no ChromaDB a partir dos PDFs na pasta 'pdfs/'."""
    os.makedirs(PASTA_PDFS, exist_ok=True)

    # 1. Apaga a pasta chroma_db antiga para eliminar vetores de PDFs removidos
    if os.path.exists(DIRETORIO_DB):
        try:
            shutil.rmtree(DIRETORIO_DB)
            print(f"Banco antigo em '{DIRETORIO_DB}' resetado para re-indexação.")
        except Exception as e:
            print(f"Aviso ao limpar diretório do banco: {e}")

    # 2. Busca todos os PDFs atualmente na pasta pdfs/
    arquivos_pdf = [os.path.join(PASTA_PDFS, f) for f in os.listdir(PASTA_PDFS) if f.lower().endswith('.pdf')]

    # Caso a pasta esteja vazia, encerra informando a limpeza
    if not arquivos_pdf:
        print("Nenhum arquivo PDF restou na pasta. O banco vetorial está limpo.")
        return None

    textos_paginas = []
    metadados = []

    for caminho_pdf in arquivos_pdf:
        nome_arquivo = os.path.basename(caminho_pdf)
        print(f"Processando: {nome_arquivo}...")
        leitor = PdfReader(caminho_pdf)
        for pagina in leitor.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                textos_paginas.append(texto_pagina)
                metadados.append({"source": nome_arquivo})

    if not textos_paginas:
        print("Nenhum texto válido foi extraído dos PDFs restantes.")
        return None

    # 3. Fatiamento do texto em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    docs = text_splitter.create_documents(textos_paginas, metadatas=metadados)
    print(f"Total de {len(docs)} chunks gerados.")

    # 4. Geração dos novos embeddings e persistência
    print("Gerando novos embeddings no ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=azure_embeddings,
        persist_directory=DIRETORIO_DB
    )
    print("Banco vetorial sincronizado com sucesso!")
    return vectorstore


@tool("Consultar Base de Conhecimento PDF")
def consultar_base_conhecimento(query: str) -> str:
    """Útil para consultar informações presentes nos documentos PDF cadastrados."""
    if not os.path.exists(DIRETORIO_DB):
        return "Nenhum documento cadastrado na base de conhecimento no momento."

    vectorstore = Chroma(
        persist_directory=DIRETORIO_DB,
        embedding_function=azure_embeddings
    )

    resultados = vectorstore.similarity_search(query, k=3)

    if not resultados:
        return "Nenhuma informação relevante foi encontrada na base de conhecimento."

    return "\n\n---\n\n".join([doc.page_content for doc in resultados])


if __name__ == "__main__":
    processar_pdf()