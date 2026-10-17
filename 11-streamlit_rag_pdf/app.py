import streamlit as st # Cria a interface do usuário

def main():
    st.set_page_config ( page_title="ChatbotPDF",page_icon=":books:")

    # Personalização das cores
    st.markdown("""
        <style>
        /* Fundo principal */
        .stApp {
            background-color: #FFFFFF;
            color: #6B4B85;
        }

        /* Sidebar lilás suave */
        [data-testid="stSidebar"] {
            background-color: #E9D5FF;
        }

        /* Texto da sidebar */
        [data-testid="stSidebar"] * {
            color: #765493;
        }

        /* Títulos */
        h1, h2, h3 {
            color: #9363B8;
        }

        /* Textos e rótulos */
        p, label {
            color: #765493;
        }

        /* Botões */
        .stButton > button {
            background-color: #B58AD6;
            color: #FFFFFF;
            border: 1px solid #A477C8;
            border-radius: 8px;
        }

        .stButton > button:hover {
            background-color: #9F70C4;
            color: #FFFFFF;
            border-color: #9363B8;
        }

      
/* Área completa de upload */
[data-testid="stFileUploader"] {
    background-color: #F8F1FF;
    border: 1px solid #DCC5F0;
    border-radius: 12px;
    padding: 12px;
}

/* Área interna onde o arquivo é carregado */
[data-testid="stFileUploader"] section {
    background-color: #F8F1FF;
    border: 1px dashed #B58AD6;
    border-radius: 10px;
}

/* Botão Browse files */
[data-testid="stFileUploader"] button {
    background-color: #DCC5F0;
    color: #5B3B75;
    border: 1px solid #B58AD6;
    border-radius: 8px;
}

/* Efeito ao passar o mouse */
[data-testid="stFileUploader"] button:hover {
    background-color: #C9A8E5;
    color: #4A2D63;
    border-color: #A477C8;
}

/* Textos da área de upload */
[data-testid="stFileUploader"] * {
    color: #765493;
}
        }

        /* Borda do upload */
        [data-testid="stFileUploader"] section {
            border-color: #C4A1E5;
        }
        </style>
    """, unsafe_allow_html=True)

# Criar barra lateral esquerda da aplicação
with st.sidebar:
    st.subheader("Seus Arquivos")
    pdf_docs=st.file_uploader("Carregar arquivos PDF",type="pdf",label_visibility="visible",accept_multiple_files=True)

    print(pdf_docs)

    if st.button("Processar"):
        pass

    if __name__== "__main__":
        main()