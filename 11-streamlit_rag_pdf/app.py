import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from utils import funcoes_texto
from utils import funcoes_chatbot

def main():
    st.set_page_config(
        page_title="ChatbotPDF",
        page_icon="📚",
        layout="centered"
    )

    # Estilo Estético: Pastel & Glassmorphism
    st.markdown("""
        <style>
        /* Fundo Principal: Branco com toque de lavanda */
        .stApp {
            background-color: #F5F3FF;
            color: #2E1065;
        }

        /* Container principal com efeito Glassmorphism */
        [data-testid="stAppViewBlockContainer"] {
            background-color: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 24px;
            box-shadow: 0 8px 32px 0 rgba(46, 16, 101, 0.05);
            padding: 3rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            border: 1px solid #DDD6FE;
        }

        /* Painéis e Sidebar com transparência */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-right: 1px solid #DDD6FE;
        }

        [data-testid="stSidebar"] * {
            color: #2E1065;
        }

        [data-testid="stHeader"] {
            background-color: transparent;
        }

        /* Texto Principal */
        h2, h3, p, label {
            color: #2E1065 !important;
        }

        /* Destaque / Botão Ativo */
        .stButton > button {
            background-color: #7C3AED;
            color: #FFFFFF !important;
            border: none;
            border-radius: 12px;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
        }

        /* Destaque Secundário (Hover do Botão) */
        .stButton > button:hover {
            background-color: #C084FC;
            color: #FFFFFF !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(192, 132, 252, 0.3);
        }

        /* Estilização do Uploader de Arquivos para o modo Glassmorphism */
        [data-testid="stFileUploader"] {
            background-color: rgba(255, 255, 255, 0.5);
            border: 1px solid #DDD6FE;
            border-radius: 16px;
            padding: 12px;
        }

        [data-testid="stFileUploader"] section {
            background-color: transparent;
            border: 2px dashed #C084FC;
            border-radius: 12px;
        }

        [data-testid="stFileUploader"] button {
            background-color: #F5F3FF;
            color: #7C3AED !important;
            border: 1px solid #DDD6FE;
            border-radius: 12px;
            font-weight: 500;
        }

        [data-testid="stFileUploader"] button:hover {
            background-color: #DDD6FE;
            color: #2E1065 !important;
        }
        
        /* Corrigindo a cor dos itens de arquivo já anexados */
        [data-testid="stFileUploader"] * {
            color: #2E1065;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título com os livrinhos coloridos e tipografia elegante
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="
                font-size: 3.5rem;
                color: #2E1065;
                font-weight: 800;
                margin-bottom: 0;">
                📚 ChatbotPDF
            </h1>
            <p style="color: #7C3AED; font-size: 1.1rem; margin-top: 5px; font-weight: 500;">
                O seu assistente inteligente para documentos
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Barra lateral esquerda (PROCESSO INTACTO)
    with st.sidebar:
        st.subheader("Seus Arquivos")

        pdf_docs = st.file_uploader(
            "Carregar arquivos PDF",
            type=["pdf"],
            label_visibility="visible",
            accept_multiple_files=True
        )

        if st.button("Processar"):
            if pdf_docs:
                try:
                    with st.spinner("Lendo e processando os PDFs..."):
                        texto_completo = funcoes_texto.ler_pdf(pdf_docs)
                        chunks = funcoes_texto.criar_texto_chunks(texto_completo)

                    st.success("PDFs processados com sucesso!")

                    # Os prints aparecem apenas no terminal do VS Code
                    print(f"Quantidade de chunks: {len(chunks)}")
                    print(chunks)

                    vectorstore = funcoes_chatbot.criar_vectorstores(chunks)
                    print(vectorstore)

                except Exception as erro:
                    st.error(f"Erro ao processar os PDFs: {erro}")
            else:
                st.warning("Carregue pelo menos um arquivo PDF.")

if __name__ == "__main__":
    main()