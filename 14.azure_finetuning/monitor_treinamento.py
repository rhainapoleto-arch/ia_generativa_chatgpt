import os
import time
from dotenv import load_dotenv
from openai import AzureOpenAI

# Carrega as credenciais do seu arquivo .env
load_dotenv()

# Inicializa o cliente do Azure OpenAI
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Cole aqui o ID do job de fine-tuning que você pegou no portal do Azure
job_id = "ftjob-074dc4a3cd0241eebc8131fa001bcb88"

print(f"Iniciando o monitoramento do job: {job_id}")

status_atual = "running"  # Status inicial genérico para entrar no loop

# O loop continua rodando enquanto o treinamento não for finalizado
while status_atual not in ["succeeded", "failed", "cancelled"]:
    # Consulta o status atualizado diretamente no Azure
    status_obj = client.fine_tuning.jobs.retrieve(job_id)
    status_atual = status_obj.status
    
    print(f"Status atual: {status_atual}...")
    
    # Se ainda estiver rodando, aguarda 30 segundos antes de checar de novo
    if status_atual not in ["succeeded", "failed", "cancelled"]:
        time.sleep(30)

# Mensagem final quando o processo encerra
if status_atual == "succeeded":
    print("\n Treinamento concluído com sucesso!")
    print(f"Modelo final gerado: {status_obj.fine_tuned_model}")
else:
    print(f"\n O treinamento encerrou com o status: {status_atual}")