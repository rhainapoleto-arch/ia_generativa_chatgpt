import os # 1. para acessar variáveis de ambiente do sistema operacional
from dotenv import load_dotenv # 1. para carregar variáveis de ambiente de forma segura
from crewai import LLM # 2. orquestração de agentes autônomos, para definir agentes, tarefas e fluxos de execução (crews), além de incluir a classe LLM
from langchain_openai import AzureOpenAIEmbeddings # 2. voltado para integração com os modelos da OpenAI e da Azure OpenAI

# 1. Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# 2. Configura o modelo LLM da Azure para uso com o CrewAI
azure_llm = LLM(
    model=f"azure/{os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME')}",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

# 3. Configura o modelo de Embeddings da Azure OpenAI para o ChromaDB
azure_embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

print("Conexão com Azure OpenAI e CrewAI configurada com sucesso!")
