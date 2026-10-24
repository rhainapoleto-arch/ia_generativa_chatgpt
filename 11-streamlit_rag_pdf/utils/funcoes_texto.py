

from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter


def ler_pdf(arquivos):
    text = ""  # Armazena o texto extraído dos PDFs

    for arquivo in arquivos:
        paginas_pdf = PdfReader(arquivo)

        for pagina in paginas_pdf.pages:
            conteudo = pagina.extract_text()

            if conteudo:
                text += conteudo + "\n"

    return text


def criar_texto_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", # Separador entre os textos
        chunk_size=1500, # Quantidade máxima de caracteres po fatia
        chunk_overlap=300, # Sobreposição do bloco anterior, interpolação
        length_function=len # Mostrar ao nosso splitter o tamanho da fatia
    )

    chunks = text_splitter.split_text(text)

    return chunks
