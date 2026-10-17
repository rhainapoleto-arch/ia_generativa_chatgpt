# Importando as bibliotecas
import os 
from dotenv import load_dotenv # Serve para carregar as variáveis de ambiente
from openai import AzureOpenAI
import numpy as np 

# Carregar as variáveis do arquivo .env
load_dotenv()

# Carregando o modelo da Azure OpenAI
modelo = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME="text-embedding-3-small"

# Função para gerar embeddings
def gerar_embedding(texto,engine):
    response = modelo.embeddings.create(
        input=[texto],
        model=engine
    )

    print(type(response.data[0]))
    print(response.data[0].model_dump())

    return response.data[0].embedding

# Lista de palavras que serão transformadas em embeddings
palavras = ["casa", "cachorro", "gato", "lobo", "leão", "zebra", "tigre"]

dicionario={}

for palavra in palavras: 
    dicionario[palavra] = gerar_embedding(palavra,
    engine=DEPLOYMENT_NAME)
    print(f"Chave-Palavra:{palavra} | Dimensões do vetor: {len
    (dicionario[palavra])}")

    print(dicionario.keys())

    print(f"Primeiros 10 valores de {palavra  }:\n{dicionario[palavra][:10]}")
    print("\n")
    print("Número de dimensões do embedding:\n",len(dicionario[palavra]))

# Palavra nova de comparação
n_palavra = "canino"
palavra_comparar = "cachorro"

n_palavra_embed = gerar_embedding(n_palavra,engine=DEPLOYMENT_NAME)

v1=np.array(dicionario[palavra_comparar])
v2=np.array(n_palavra_embed)

similaridade = np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))

print(f"Semelhança entre {n_palavra} e {palavra_comparar}:{similaridade:.2f}")

# Soma de Vetores
v_leao=np.array(dicionario["leão"])
v_zebra=np.array(dicionario["zebra"])
vetor_soma= v_leao + v_zebra

print("Comparando o conceito(Leão+Zebra)")
for palavra,vetor in dicionario.items():
    v_palavra =np.array(vetor)

    similar = np.dot(v_palavra,vetor_soma)/(np.linalg.norm(v_palavra))*np.linalg.norm(vetor_soma)

    print(f"{palavra}: {similar:.2f}")