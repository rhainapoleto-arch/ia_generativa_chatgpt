import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import time

# Carrega as variáveis do arquivo .env para o ambiente do Python
load_dotenv()

# Inicializa o cliente do Azure OpenAI usando as credenciais do .env
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

print("Conexão estabelecida com sucesso via .env!")

print("Iniciando o upload do arquivo de treinamento...")

# 1. Faz o upload do arquivo .jsonl para o Azure
# rb significa "read binary", que é o modo de leitura de arquivos binários
with open("recursos/infraestrutura.jsonl", "rb") as arquivo_treino:
    # O método client.files.create é usado para enviar o arquivo para o Azure OpenAI
    resposta_upload = client.files.create(
        file=arquivo_treino, # O arquivo que será enviado
        purpose="fine-tune" # Indica que o arquivo será usado para ajuste fino 
    )

file_id = resposta_upload.id
print(f"Arquivo enviado com sucesso! ID do arquivo: {file_id}")

print("Disparando o trabalho de fine-tuning...")

# 2. Cria o job de ajuste fino
# O método client.fine_tuning.jobs.create é usado para iniciar o processo de fine-tuning
resposta_job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-4o-mini"
)

print(f"Trabalho de fine-tuning criado com ID: {resposta_job.id}") # Exibe o ID do job de fine-tuning criado
print(f"Status atual: {resposta_job.status}") # Exibe o status atual do job de fine-tuning

job_id = resposta_job.id
print(f"Trabalho de fine-tuning criado com ID: {job_id}")

# Início do bloco de monitoramento
print("Aguardando o término do treinamento...")

status_atual = resposta_job.status

# O loop continua rodando enquanto o status não for finalizado
while status_atual not in ["succeeded", "failed", "cancelled"]:
    # Consulta o status atualizado do job no Azure
    status_obj = client.fine_tuning.jobs.retrieve(job_id)
    status_atual = status_obj.status
    
    print(f"Status atual: {status_atual}...")
    
    # Aguarda 30 segundos antes de verificar novamente
    if status_atual not in ["succeeded", "failed", "cancelled"]:
        time.sleep(30)

# Mensagem final baseada no resultado
if status_atual == "succeeded":
    print("\n Treinamento concluído com sucesso!")
    print(f"Modelo final gerado: {status_obj.fine_tuned_model}")
else:
    print(f"\n O treinamento encerrou com o status: {status_atual}")