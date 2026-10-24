import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import RunablePassthrough
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser

def criar_vectorstores(chunks): 
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION") # Corrigido aqui
    )

    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore

def criar_chatbot_chain(vectorstore):
    llm=AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature= 0.0
    )

    retriever - vectorstore.as_retriver()

    def formatar_vetor_texto(trecho_recuperado):
        return "\n\n".join(trecho.pag_content for trecho in trecho_recuperado)
    
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
        Você é um assistente de inteligência artificial especializado em responder dúvidas com base em documentos internos.

        DIRETRIZES:
        1. **Fonte da Verdade:** Responda à pergunta do usuário usando **apenas** o Contexto fornecido abaixo.
        2. **Ausência de Informação:** Se a resposta não estiver clara ou presente no contexto, responda exatamente: "Desculpe, não encontrei informações sobre isso nos documentos fornecidos."
        3. **Proibido Alucinar:** Não use conhecimentos prévios ou externos para responder. Atenha-se estritamente ao texto recuperado.
        4. **Tom e Estilo:** Seja claro, objetivo, cordial e utilize formatação em Markdown (tópicos e negrito) para facilitar a leitura.
            """   
            "Com base exclusivamente nos documentos fornecidos: \n\n {base_conhecimento}"     
        ),
        MessagesPlaceholder(variable_name="chat_history"), ("human",{input})
        
    ])

